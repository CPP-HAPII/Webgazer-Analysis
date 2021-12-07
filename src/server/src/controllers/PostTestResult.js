const {testresult} = require('../models')

module.exports = {
  async postTestResult (req, res) {
    try {
      await testresult.create(req.body).then(result => {
        res.send(result)
      })
    } catch (err) {
      res.status(400).send({
        error: 'Unable to create testresult'
      })
    }
  }
}
