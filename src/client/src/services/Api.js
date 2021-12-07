import axios from 'axios'

export default() => {
  return axios.create({
    baseURL: `https://backend.cpphappiwebapp.com/`
    // baseURL: `http://54.193.20.125:8081/`
  })
}
