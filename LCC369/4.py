
import copy

def solution(queries):
    result = []
    
    dbts = {} # database timestamp
    
    database = {}
    
    
    
    for q in queries:
        ops = q[0]
        
        if ops == "SET":
            ts, key, field, value = q[1:]
            
            timestamp = int(ts)
            
            if key not in database:
                database[key] = {}
            database[key][field] = (value, float('inf'))
            result.append("")
            
            dbts[timestamp] = copy.deepcopy(database)
            
        elif ops == "COMPARE_AND_SET":
            ts, key, field, expectedV, newV = q[1:]
            
            currentTime = int(ts)
            timestamp = int(ts)
            
            if key not in database or field not in database[key]:
                result.append("false")
            else:
                currentV, ttl = database[key][field] # ttl is ignored here
                
                if currentTime < ttl and currentV == expectedV:
                    database[key][field] = (newV, float('inf'))
                    result.append("true")
                else:
                    result.append("false")
            dbts[timestamp] = copy.deepcopy(database)
                                
        elif ops == "COMPARE_AND_DELETE":
            ts, key, field, expectedV = q[1:]
            currentTime = int(ts)
            timestamp = int(ts)
            if key not in database or field not in database[key]:
                result.append("false")
            else:
                currentV, ttl = database[key][field] # ttl is ignored here
                
                if currentTime < ttl and currentV == expectedV:
                    tmpDB = database[key]
                    del tmpDB[field]
                    database[key] = tmpDB
                    result.append("true")
                else:
                    result.append("false")
            dbts[timestamp] = copy.deepcopy(database)
                    
        elif ops == "GET":
            ts, key, field = q[1:]
            timestamp = int(ts)
            currentTime = int(ts)
            if key not in database or field not in database[key]:
                result.append("")
            else:
                currentV, lastTimeToAlive = database[key][field]  # ttl is ignored here
                if currentTime < lastTimeToAlive: 
                    result.append(currentV)
                else:
                    result.append("")
            dbts[timestamp] = copy.deepcopy(database)
                
        
        elif ops == "SCAN":
            ts, key = q[1:]
            currentTime = int(ts)
            timestamp = int(ts)
            if key not in database:
                result.append("")
            else:
                retVal = ""
                tmpDict = database[key]
                n = len(tmpDict)
                for i, (k, v) in enumerate(sorted(tmpDict.items())):
                    v, ttl = v
                    if currentTime < ttl:
                        if retVal != "":
                            retVal+=", "
                        retVal += str(k)+"("+str(v)+")"
                        
                result.append(retVal)
            dbts[timestamp] = copy.deepcopy(database)
                    
        elif ops == "SCAN_BY_PREFIX":
            ts, key, prefix = q[1:]
            currentTime = int(ts)
            timestamp = int(ts)
            if key not in database:
                result.append("")
            else:
                retVal = ""
                tmpDict = database[key]
                n = len(tmpDict)
                for i, (k, v) in enumerate(sorted(tmpDict.items())):
                    v, ttl = v   
                    if currentTime < ttl and k.startswith(prefix):           
                        if retVal != "":
                            retVal+=", " 
                        retVal += str(k)+"("+str(v)+")"
                
                result.append(retVal)
            dbts[timestamp] = copy.deepcopy(database)
        
        
        elif ops == "SET_WITH_TTL":
            ts, key, field, value, ttl = q[1:]
            lastAliveTimeStamp = int(ts) + int(ttl)
            timestamp = int(ts)
            
            if key not in database:
                database[key] = {}
            database[key][field] = (value, lastAliveTimeStamp)
            result.append("")
            dbts[timestamp] = copy.deepcopy(database)
            
        
        elif ops == "COMPARE_AND_SET_WITH_TTL":
            ts, key, field, expectedV, newV, ttl = q[1:]
            lastAliveTimeStamp = int(ts) + int(ttl)
            currentTime = int(ts)
            timestamp = int(ts)
            
            if key not in database or field not in database[key]:
                result.append("false")
            else:
                currentV, ttl = database[key][field] # ttl is ignored here
                
                if currentTime < ttl and currentV == expectedV:
                    database[key][field] = (newV, lastAliveTimeStamp)
                    result.append("true")
                else:
                    result.append("false")
            dbts[timestamp] = copy.deepcopy(database)
        
        elif ops == "GET_WHEN":
            ts, key, field, atts = q[1:]
            
            print(q)
            atts = int(atts)
            timestamps = list(dbts.keys())
            timestamps.sort()
            print(timestamps)
            
            if atts == 0:
                currentTime = int(ts)
                if key not in database or field not in database[key]:
                    result.append("")
                else:
                    currentV, lastTimeToAlive = database[key][field]  # ttl is ignored here
                    if currentTime < lastTimeToAlive: 
                        result.append(currentV)
                    else:
                        result.append("")
            
            elif not timestamps:
                # nothing should exist here
                result.append("")
            else:
                suitableStamp = None
                for t in timestamps:
                    if t<=atts:
                        suitableStamp = t
                    else:
                        break
                if suitableStamp is None:
                    result.append("")
                else:
                    print(suitableStamp)
                    dbsnap = dbts[suitableStamp]
                    # Regular GET
                    if key not in dbsnap or field not in dbsnap[key]:
                        result.append("")
                    else:
                        print(dbsnap[key], suitableStamp)
                        currentV, lastTimeToAlive = dbsnap[key][field]  # ttl is ignored here
                        if atts < lastTimeToAlive:
                            print("ADDING....", currentV)
                            result.append(currentV)
                        else:
                            result.append('')
            dbts[int(ts)] = copy.deepcopy(database)
      
            
    return result

queries=[
      [
        "SET_WITH_TTL",
        "160000005",
        "key1",
        "field1",
        "1",
        "95"
      ],
      [
        "SET_WITH_TTL",
        "160000006",
        "key1",
        "field2",
        "2",
        "44"
      ],
      [
        "SET_WITH_TTL",
        "160000007",
        "key2",
        "field1",
        "3",
        "33"
      ],
      [
        "SET_WITH_TTL",
        "160000008",
        "key3",
        "field1",
        "4",
        "82"
      ],
      [
        "SET_WITH_TTL",
        "160000009",
        "key3",
        "field2",
        "5",
        "103"
      ],
      [
        "SET_WITH_TTL",
        "160000010",
        "key3",
        "final",
        "6",
        "200"
      ],
      [
        "SCAN",
        "160000011",
        "key3"
      ],
      [
        "COMPARE_AND_SET_WITH_TTL",
        "160000020",
        "key1",
        "field2",
        "2",
        "7",
        "40"
      ],
      [
        "COMPARE_AND_SET_WITH_TTL",
        "160000021",
        "key2",
        "field1",
        "3",
        "8",
        "29"
      ],
      [
        "COMPARE_AND_SET",
        "160000022",
        "key3",
        "field1",
        "4",
        "151"
      ],
      [
        "COMPARE_AND_SET_WITH_TTL",
        "160000023",
        "key3",
        "field1",
        "151",
        "92",
        "70"
      ],
      [
        "GET",
        "160000030",
        "key1",
        "field1"
      ],
      [
        "SCAN_BY_PREFIX",
        "160000080",
        "key3",
        "fie"
      ],
      [
        "COMPARE_AND_SET_WITH_TTL",
        "160000082",
        "key1",
        "field2",
        "5",
        "7",
        "100"
      ],
      [
        "COMPARE_AND_DELETE",
        "160000085",
        "key3",
        "field2",
        "5"
      ],
      [
        "SET_WITH_TTL",
        "160000087",
        "key2",
        "field1",
        "8",
        "100"
      ],
      [
        "COMPARE_AND_SET_WITH_TTL",
        "160000100",
        "key4",
        "field1",
        "0",
        "50",
        "90"
      ],
      [
        "SCAN",
        "160000110",
        "key1"
      ],
      [
        "GET_WHEN",
        "160000192",
        "key1",
        "field1",
        "160000097"
      ],
      [
        "GET_WHEN",
        "160000200",
        "key2",
        "field1",
        "160000055"
      ],
      [
        "GET_WHEN",
        "160000210",
        "key3",
        "field1",
        "160000024"
      ],
      [
        "GET_WHEN",
        "160000220",
        "key3",
        "field1",
        "160000022"
      ],
      [
        "GET_WHEN",
        "160000230",
        "key1",
        "field2",
        "160000082"
      ]
    ]
# ["", "", "", "", "", "", "30", "", "72", "", "false", "", "", "key1(25), key3(1)", "72", "25"]

print(solution(queries))