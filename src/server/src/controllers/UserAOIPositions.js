const {userAOIPositions} = require('../models')

module.exports = {
  async userAOIPositions (req, res) {
    try {
      await userAOIPositions.create(req.body).then(result => {
        res.send(result)
      })
    } catch (err) {
      res.status(400).send({
        error: `Unable to create userAOIPositions ${err.toString()}`
      })
    }
  }
}