
const basewest = "http://westteam.nulstar.com/tokenlife/"
const baselocal = "http://localhost:8084/"
const stat = "static/plot"
const pub = "public/plots/plot"

const weststat = basewest + stat
const westpub = basewest + pub
const localstat = baselocal + stat
const localpub = baselocal + pub

// uncomment your choice and comment out others:

// const bstr = weststat
// const bstr = westpub
const bstr = localstat
// const bstr = localpub

export default {
  data: {
    bstr,
  }
}
