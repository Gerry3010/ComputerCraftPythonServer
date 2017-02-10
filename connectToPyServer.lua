local url = 'http://localhost:4343/'

server_on = http.get(url .. 'hello/')

if server_on == nil then
    print('PyServer is off')
    return
else
    print('PyServer ready')
end

local command_string = ''
local command_id = ''

function tableToString(tbl)
    local str = '{'
    for k, v in pairs(tbl) do
        str = str .. tostring(k) .. ':'
        if type(v) == 'table' then
            str = str .. tableToString(v)
        else
            str = str .. tostring(v)
        end
        str = str .. ','
    end
    str = str .. '}'

    return str
end

function handler()
    print('executing "' .. command_string .. '" (' .. command_id .. ')...')
    local cmd_result1, cmd_result2 = loadstring('return ' .. command_string)()

    local query_string = 'result=' .. tostring(cmd_result1)
    if cmd_result2 then
        if type(cmd_result2) == 'table' then
            query_string = query_string .. '&result2=' .. tableToString(cmd_result2)
        else
            query_string = query_string .. '&result2=' .. tostring(cmd_result2)
        end
    end

    query_string = query_string .. '&id=' .. command_id

    http.post(url, query_string)
end

function errorhandler(err)
    http.post(url, 'error=' .. err .. '&id=' .. command_id)
    print('Error: ' .. err)
end

local message

function loadmessage()
    message = http.get(url).readAll()
end

while true do
    pcall(loadmessage)
    if message then
        print('Message: ' .. message)
        local commaindex = string.find(message, ',')
        if commaindex then
            command_id = string.sub(message, 0, commaindex - 1)
            command_string = string.sub(message, commaindex + 1, string.len(message))

            xpcall(handler, errorhandler)
        end
        message = nil
    end
end
