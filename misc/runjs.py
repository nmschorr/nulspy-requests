from Naked.toolshed.shell import execute_js, muterun_js
import asyncio
from time import sleep
#
# scripty = 'E:\\nulsjs\\lib\\test\\verifyAddress.js'
#
# scripty2 = 'E:\\nulsjs\\src\\test\\addressByPub.js'
#
# scripty3 = 'E:\\nulsjs\\src\\test\\newAddress.js'
#
# #s4 = 'E:\\nulsjs\\src\\test\\getBalance(chain, assetChainId = 2, assetId = 1, address)
# addy= "TTSETeCA3Fdhsu91EFmTuwHpXaNfWgUDL35sZS7"
#
#
# jsfile = "E:\\nulsjs\\src\\test\\getBalance.js"
#
# s4 = "require"
#
# args = 'chain, assetChainId = 2, assetId = 1, address=addy'
# # success = execute_js('testscript.js')


#
# success = execute_js(s4)
# assetChainId, assetId, address
# success = muterun_js(s4, arguments=args)

# success = muterun_js(jsfile)
# sleep(2)
# E:\nulsjs\src\test\getBalance.js
#b"internal/modules/cjs/loader.js:796\r\n    throw err;\r\n    ^\r\n\r\nError:
# Cannot find module './https.js'\r\nRequire stack:\r\n- E:\\nulsjs\\src\\test\\getBalance.js\r\n    at Function.Module._resolveFilename (internal/modules/cjs/loader.js:793:17)\r\n    at Function.Module._load (internal/modules/cjs/loader.js:686:27)\r\n    at Module.require (internal/modules/cjs/loader.js:848:19)\r\n    at require (internal/modules/cjs/helpers.js:74:18)\r\n    at Object.<anonymous> (E:\\nulsjs\\src\\test\\getBalance.js:3:12)\r\n    at Module._compile (internal/modules/cjs/loader.js:955:30)\r\n    at Object.Module._extensions..js (internal/modules/cjs/loader.js:991:10)\r\n    at Module.load (internal/modules/cjs/loader.js:811:32)\r\n    at Function.Module._load (internal/modules/cjs/loader.js:723:14)\r\n    at Function.Module.runMain (internal/modules/cjs/loader.js:1043:10) {\r\n  code: 'MODULE_NOT_FOUND',\r\n
# requireStack: [ 'E:\\\\nulsjs\\\\src\\\\test\\\\getBalance.js' ]\r\n}\r\n"

# E:\nulsjs\src\test-originaldir\transfer.js


jsfile = 'E:\\nulsjs\\src\\test-originaldir\\transfer.js'
jsfile2 = 'E:\\nulsjs\\src\\test-originaldir\\api\\getBalance.js'


response = muterun_js(jsfile2)
sleep(2)
print(response)
sleep(2)