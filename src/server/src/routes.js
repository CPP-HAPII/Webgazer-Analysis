const GetQuery = require('./controllers/GetQuery')
const GetResults = require('./controllers/GetResults')
const PostRelevance = require('./controllers/PostRelevance')
const PostDemographic = require('./controllers/PostDemographic')
const PostTestResult = require('./controllers/PostTestResult')
const Authentication = require('./controllers/Authentication.js')
const GetQuestions = require('./controllers/GetQuestions.js')
const PostQuestionnaire = require('./controllers/PostQuestionnaire.js')
const Testing = require('./controllers/test.js')
const Page = require('./controllers/Page.js')
const UserAOIPositions = require('./controllers/UserAOIPositions.js')
const UserGaze = require('./controllers/UserGaze.js')

module.exports = (app) => {
  app.get('/queries',
    GetQuery.getQueries)
  app.post('/query',
    GetQuery.getQuery)
  app.get('/query/:qID',
    GetQuery.show)
  app.post('/results',
    GetResults.getResults)
  app.post('/relevances',
    PostRelevance.postRelevances)
  app.post('/relevance',
    PostRelevance.postRelevance)
  app.post('/register',
    Authentication.createUser)
  app.post('/questions',
    GetQuestions.getQuestions)
  app.post('/testing',
    Testing.testJoin)
  app.post('/demographic',
    PostDemographic.postDemographic)
  app.post('/postQuestions', 
    PostQuestionnaire.postQuestionnaire)
  app.post('/page',
    Page.postPage)
  app.post('/pageUpdate',
    Page.updatePage),
  app.post('/testresult',
    PostTestResult.postTestResult),
  app.post('/userAOIPositions',
    UserAOIPositions.userAOIPositions),
  app.post('/userGaze',
    UserGaze.userGaze)
}
