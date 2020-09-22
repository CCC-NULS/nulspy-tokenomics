// edit this only!
// const WESTTEAM = true
const WESTTEAM = true
// end user edits - = - =  - = - = - = - = - = - = - = - = - = - = - = - = - = - = //

// var westPortOnly = "8084"
// var homePort = "8084"

var thePort = "8084"

var westIP = "https://0.0.0.0"  //westteam   "http://116.202.157.151"
var homeIP = "http://127.0.0.1"        //home  "http://127.0.0.1" 

var westIPwPORT =  `${westIP}:${thePort}`  // west
var homeIPwPORT = `${homeIP}:${thePort}` // home

// - = - =  - = - = - = - = - = - = - = - = - = - = - = - = - = - = //
var westDirStr = `/tokenlife/static/plot` //  doesn't need port on westteam because nginx is serving image
var homeDirStr = `/static/plot`

var homeIMAGEp1 = `${homeIP}:${thePort}${homeDirStr}`;  //  home needs port # because of flask                
var westIMAGEp1 = `${westIP}${westDirStr}`;  // westteam - nginx-only for viewing image

var finalIPwPORT
var finalIMAGEp1

if (WESTTEAM) {
  finalIPwPORT = westIPwPORT  // west
  finalIMAGEp1 = westIMAGEp1   // west   
}
else { 
  finalIPwPORT = homeIPwPORT  // home
  finalIMAGEp1 = homeIMAGEp1   // home

}
  
export { finalIPwPORT }
export { finalIMAGEp1 }
console.log("finalIPwPORT in constants: " + finalIPwPORT)
console.log("finalIMAGEp1 in constants: " + finalIMAGEp1)


export var acceptstretc = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
export var getpostetc = "GET, POST, OPTIONS";
export var accessmethods = "Access-Control-Allow-Methods";
export var accesscontrol = "Access-Control-Allow-Origin";
export var plaintext = "text/plain; charset=utf-8";
export var contenttype = "Content-Type";

export var maxage = "Access-Control-Max-Age";   // preflight only
export var maxageval = 1728000;
export var aclh = "Access-Control-Allow-Headers";
export var aclhlist = "'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range";



//         add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range';
//         add_header 'Access-Control-Expose-Headers' 'Content-Length,Content-Range';

// #
// # Wide-open CORS config for nginx
// #
// location / {
//      if ($request_method = 'OPTIONS') {
//         add_header 'Access-Control-Allow-Origin' '*';
//         add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
//         #
//         # Custom headers and headers various browsers *should* be OK with but aren't
//         #
//         add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range';
//         #
//         # Tell client that this pre-flight info is valid for 20 days
//         #
//         add_header 'Access-Control-Max-Age' 1728000;
//         add_header 'Content-Type' 'text/plain; charset=utf-8';
//         add_header 'Content-Length' 0;
//         return 204;
//      }
//      if ($request_method = 'POST') {
//         add_header 'Access-Control-Allow-Origin' '*';
//         add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
//         add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range';
//         add_header 'Access-Control-Expose-Headers' 'Content-Length,Content-Range';
//      }
//      if ($request_method = 'GET') {
//         add_header 'Access-Control-Allow-Origin' '*';
//         add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
//         add_header 'Access-Control-Allow-Headers' 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range';
//         add_header 'Access-Control-Expose-Headers' 'Content-Length,Content-Range';
//      }
// }