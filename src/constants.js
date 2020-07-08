
let basewest = 'http://westteam.nulstar.com/tokenlife/'
let baselocal = 'http://localhost:8084/'
let stat = 'static/plot'
let pub = 'public/plots/plot'

let weststat = basewest + stat
let westpub = basewest + pub
let localstat = "`${baselocal}${stat}`"
let localpub = baselocal + pub

// uncomment your choice and comment out others:

// const bstr = weststat
// const bstr = westpub
// let bstr = localstat
// const bstr = localpub

export default {
  data: {
    bstr: "`${localstat}`",
  }
}
