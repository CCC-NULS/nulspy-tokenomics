
export var cars = new Array("Saab", "Volvo", "BMW");
export var initsupply = new Array("100,000,000", "150,000,000", "175,000,000", "200,000,000", "225,000,000", "260,000,000", "300,000,000");
export var aninflation = new Array("2,000,000", "3,000,000", "4,000,000", "5,000,000", "6,000,000");
export var inflatervals = new Array("0", "1", "2", "3", "4", "6", "12", "18", "24", "36", "48");
export var stopinflation = new Array("50,000,000", "100,000,000", "150,000,000", "200,000,000", "250,000,000", "310,000,000", "350,000,000", "450,000,000", "510,000,000");
export var disinflation = new Array("0", "0.1%", "0.2%", "0.3%", "0.4%", "0.5%", "0.6%", "0.7%");
export var acceptStr = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
export var restTypes = "GET, POST, HEAD, UPDATE, PUT";
export var acctlMeths = "Access-Control-Allow-Methods";
export var acctlOrig = "Access-Control-Allow-Origin";
export var appJson = "application/json";
export var ctType = "Content-Type";


var westIP = "http://116.202.157.151"  //westteam   "http://116.202.157.151"
var westIPwPORT = `${westIP}:8084` // westteam
var westIMAGE = `${westIP}/tokenlife/static/plot`;  // westteam - nginx-only for viewing image
                          // image doesn't need port on westteam because nginx is serving image

var homeIP = "http://127.0.0.1"  //home  "http://127.0.0.1" 
var homeIPwPORT = `${homeIP}:8084` // home
var homeIMAGE = `${homeIPwPORT}/tokenlife/static/plot`;  //  home needs full because of flask
                         
var ISCENTOS = false
//var ISCENTOS = true

if (ISCENTOS) {
  var finIP = westIP  // west
  var finIPwPORT = westIPwPORT  // west
  var finalIMAGEp1 = westIMAGE   // west      
  }
else { 
  var finIP = homeIP  // home
  var finIPwPORT = homeIPwPORT  // home
  var finalIMAGEp1 = homeIMAGE   // home
  }

export { finIPwPORT, finalIMAGEp1 }

