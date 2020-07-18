// edit this only!
//var ISCENTOS = false
//var ISCENTOS = true
import { ISCENTOS } from  '../../../constants.js'
// end user edits - = - =  - = - = - = - = - = - = - = - = - = - = - = - = - = - = //

var westPortOnly = "8084"
var homePortOnly = "8084"
var westIP = "http://116.202.157.151"  //westteam   "http://116.202.157.151"

export var acceptStr = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
export var restTypes = "GET, POST, HEAD, UPDATE, PUT";
export var acctlMeths = "Access-Control-Allow-Methods";
export var acctlOrig = "Access-Control-Allow-Origin";
export var appJson = "application/json";
export var ctType = "Content-Type";


var westIPwPORT =  `${westIP}:${westPortOnly}`  // west

var homeIP = "http://127.0.0.1"  //home  "http://127.0.0.1" 

var homeIPwPORT = `${homeIP}:${homePortOnly}` // home

// - = - =  - = - = - = - = - = - = - = - = - = - = - = - = - = - = //

var westIMAGEp1 = `${westIP}/tokenlife/static/plot`;  // westteam - nginx-only for viewing image
                          // image doesn't need port on westteam because nginx is serving image

var homeIMAGEp1 = `${homeIP}:${homePortOnly}/static/plot`;  //  home needs port # because of flask                

var finalIPwPORT
var finalIMAGEp1

if (ISCENTOS) {
  finalIPwPORT = westIPwPORT  // west
  finalIMAGEp1 = westIMAGEp1   // west   
  
}
else { 
  finalIPwPORT = homeIPwPORT  // home
  finalIMAGEp1 = homeIMAGEp1   // home
  console.log("finalIPwPORT in constants: " + finalIPwPORT)

  console.log("finalIMAGEp1 in constants: " + finalIMAGEp1)
  }

export { finalIPwPORT }
export { finalIMAGEp1 }
