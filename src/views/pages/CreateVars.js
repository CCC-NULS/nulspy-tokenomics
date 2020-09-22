// edit this only!
// const WESTTEAM = true
const WESTTEAM = true
// end user edits - = - =  - = - = - = - = - = - = - = - = - = - = - = - = - = - = //

var theroute = "chart"

// var finalPOST = "https://westteam.nulstar.com"  //westteam   "http://116.202.157.151"
var finalPOST = "http://0.0.0.0"  //westteam   "http://116.202.157.151"

// - = - =  - = - = - = - = - = - = - = - = - = - = - = - = - = - = //
var westDirStr = `/tokenlife/static/plot` //  doesn't need port on westteam because nginx is serving image
            
var GETpartone = `${finalPOST}${westDirStr}`;  // westteam - nginx-only for viewing image
  
export { finalPOST }
export { GETpartone }
console.log("finalPOST in constants: " + finalPOST)
console.log("GETpartone in constants: " + GETpartone)

export var acceptstretc = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
export var getpostetc = "GET, POST, OPTIONS";
export var accessmethods = "Access-Control-Allow-Methods";
export var accesscontrol = "Access-Control-Allow-Origin";
export var plaintext = "text/plain; charset=utf-8";
export var contenttype = "Content-Type";

export var maxage = "Access-Control-Max-Age";   // preflight only
export var maxageval = 1728000;
export var aclh = "Access-Control-Allow-Headers";
export var aclhlist = "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range";
