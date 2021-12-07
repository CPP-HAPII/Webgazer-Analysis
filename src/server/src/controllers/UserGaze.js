const {userGaze} = require('../models')

module.exports = {
  async userGaze (req, res) {
    try {
      await userGaze.create(req.body).then(result => {
        res.send(result)
      })
    } catch (err) {
      res.status(400).send({
        error: `Unable to create userGaze: ${err.toString()}`
      })
    }
  }
}