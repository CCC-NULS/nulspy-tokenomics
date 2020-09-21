// edit this only!
// const WESTTEAM = true
const WESTTEAM = true
// end user edits - = - =  - = - = - = - = - = - = - = - = - = - = - = - = - = - = //

// var westPortOnly = "8084"
// var homePort = "8084"

var thePort = "8084"

var westIP = "https://116.202.157.151"  //westteam   "http://116.202.157.151"
var homeIP = "https://127.0.0.1"        //home  "http://127.0.0.1" 

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


export var acceptStr = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
export var restTypes = "GET, POST, HEAD, UPDATE, PUT";
export var acctlMeths = "Access-Control-Allow-Methods";
export var acctlOrig = "Access-Control-Allow-Origin";
export var appJson = "application/json";
export var ctType = "Content-Type";
