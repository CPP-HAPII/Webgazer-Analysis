import axios from 'axios'

export default() => {
  return axios.create({
    baseURL: `https://server.webgazerbackend.link/`
    // baseURL: `http://54.193.20.125:8081/` `https://backend.cpphappiwebapp.com/`
  })
}
