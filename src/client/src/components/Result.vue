<template>
  <v-container fluid grid-list-xl pt-1 px-0>
    <v-layout row align-left v-if="getID" :key="qID">
      <v-flex xs4 d-flex offset-xs4>
        <ul class="resultPage">
          <li v-for="(result, index) in results" :key="result.title">
            <!-- <div>{{result.id}}</div> -->
            <div ref="resultPos" class="resultAOI">
                <div class="title">
                  {{result.title}}
                </div>
                <div class="url">
                  {{result.url}}
                </div>
                <div class="snip">
                  {{result.snippet}}
                </div>
            </div>
            <div class="myButton">
              <relevance :num='index' :id='result.id' :language='language'/>
            </div>
          </li>
          <v-btn align="center" v-on:click="subResponse">Next</v-btn>
        </ul>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import QueryService from '@/services/QueryService'
import Relevance from '@/components/Relevance.vue'
import webgazer from 'webgazer'
var dataArray = []
export default {
  components: {
    Relevance
  },
  props: ['someID', 'language'],
  data () {
    return {
      results: [],
      clicked: [null, null, null, null, null, null],
      qID: this.$store.state.route.params.queryID,
      order: null,
      someId: null,
      isGetting: false
    }
  },
  computed: {
    getID () {
      var id = this.$store.getters.getActualQuery
      console.log(id)
      this.getResults(id)
      return id
    }
  },
  mounted () {
    // var id = this.$store.getters.getActualQuery
    // this.getResults(id)
    this.getDataArray()
  },
  methods: {
    async makePageStuff () {
      var toPost = {
        userID: this.$store.getters.getUID,
        task: parseInt(this.qID),
        qLanguage: this.language,
        order: this.order
      }

      var result = (await QueryService.page({toPost})).data
      this.someId = result.id
    },
    getDataArray: function () {
      // var aoiArray = [];
      dataArray = []
      // const LEFT_CUTOFF = window.innerWidth / 2
      // const RIGHT_CUTOFF = window.innerWidth - window.innerWidth / 2
      // let lookDirection = null
      webgazer.showVideoPreview(false).showPredictionPoints(false)
        .setGazeListener(function (data, elapsedTime) {
          if (data == null) {
            return
          }
          var xprediction = data.x // these x coordinates are relative to the viewport
          var yprediction = data.y // these y coordinates are relative to the viewport
          // array for holding the current data points per row
          var rowArray = []
          rowArray.push(elapsedTime)
          rowArray.push(xprediction)
          rowArray.push(yprediction)
          dataArray.push(rowArray)
        }).begin()
    },
    getResults: async function (myVal) {
      var r1 = (await QueryService.results({ 'id': myVal })).data
      // var q2 = myVal + 1
      var sTemp = null
      if (this.$store.getters.getLanguage === 'Spanish') {
        // changed offset to 60 since there are 60 sets of queries for each langauge
        sTemp = myVal + 60
      } else {
        if (myVal >= 135 && myVal <= 161) {
          sTemp = myVal - 60
        } else {
          sTemp = myVal + 60
        }
      }
      var r2 = (await QueryService.results({ 'id': sTemp })).data
      var uid = this.$store.getters.getUID
      var sequence = [
        [1, 2, 0, 3, 4],
        [4, 0, 3, 1, 2],
        [3, 4, 2, 0, 1],
        [2, 3, 1, 4, 0],
        [0, 1, 4, 2, 3]
      ]
      var row = uid % 5
      var column = this.$store.state.route.params.queryID % 5
      var decider = sequence[row][column]
      this.order = decider
      this.results = []
      if (decider === 0) {
        this.results = r1
      } else if (decider === 1) {
        this.results = r2
      } else if (decider === 2) {
        this.results.push(r1[0], r1[1], r1[2], r2[0], r2[1], r2[2])
      } else if (decider === 3) {
        this.results.push(r2[0], r2[1], r2[2], r1[0], r1[1], r1[2])
      } else if (decider === 4) {
        this.results.push(r1[0], r2[0], r1[1], r2[1], r1[2], r2[2])
      }
      this.makePageStuff()
    },
    // updateRelevance (newValue, index) {
    //   this.clicked[index] = newValue
    //   var toPost = {
    //     userID: this.$store.getters.getUID,
    //     resultID: this.results[index].id,
    //     rank: index,
    //     relevance: newValue
    //   }
    // QueryService.relevance(toPost)
    // },
    // **next button click event listener function
    subResponse: async function () {
      // var toSave = []
      // var rel = ['Definitely Relevant', 'Possibly Relevant', 'Not Relevant']
      // for (var index = 0; index < 6; index++) {
      //   var result = {
      //     userID: this.$store.getters.getUID,
      //     // Make sure to fix resultID
      //     resultID: index * 10,
      //     rank: index,
      //     relevance: rel[this.clicked[index]]
      //   }
      //   toSave.push(result)
      // }
      // console.log(toSave)
      // QueryService.relevance(toSave)

      await QueryService.pageUpdate({id: this.someId})
      // gets left and right positions of AOI's, should be the same for all AOI's
      const leftPos = this.$refs.resultPos[0].getBoundingClientRect().left
      const rightPos = this.$refs.resultPos[0].getBoundingClientRect().right
      console.log('Left Pos: ' + leftPos + ', Right Pos: ' + rightPos)
      // gets the first AOI's top and bottom positions
      const topPos1 = this.$refs.resultPos[0].getBoundingClientRect().top
      const bottomPos1 = this.$refs.resultPos[0].getBoundingClientRect().bottom
      console.log('Top Pos 1: ' + topPos1 + ', Bottom Pos 1: ' + bottomPos1)
      // gets the second AOI's top and bottom positions
      const topPos2 = this.$refs.resultPos[1].getBoundingClientRect().top
      const bottomPos2 = this.$refs.resultPos[1].getBoundingClientRect().bottom
      console.log('Top Pos 2: ' + topPos2 + ', Bottom Pos 2: ' + bottomPos2)
      // gets the third AOI's top and bottom positions
      const topPos3 = this.$refs.resultPos[2].getBoundingClientRect().top
      const bottomPos3 = this.$refs.resultPos[2].getBoundingClientRect().bottom
      console.log('Top Pos 3: ' + topPos3 + ', Bottom Pos 3: ' + bottomPos3)
      // gets the fourth AOI's top and bottom positions
      const topPos4 = this.$refs.resultPos[3].getBoundingClientRect().top
      const bottomPos4 = this.$refs.resultPos[3].getBoundingClientRect().bottom
      console.log('Top Pos 4: ' + topPos4 + ', Bottom Pos 4: ' + bottomPos4)
      // gets the fifth AOI's top and bottom positions
      const topPos5 = this.$refs.resultPos[4].getBoundingClientRect().top
      const bottomPos5 = this.$refs.resultPos[4].getBoundingClientRect().bottom
      console.log('Top Pos 5: ' + topPos5 + ', Bottom Pos 5: ' + bottomPos5)
      // gets the sixth AOI's top and bottom positions
      const topPos6 = this.$refs.resultPos[5].getBoundingClientRect().top
      const bottomPos6 = this.$refs.resultPos[5].getBoundingClientRect().bottom
      console.log('Top Pos 6: ' + topPos6 + ', Bottom Pos 6: ' + bottomPos6)
      // stores aoi positions into useraoipositions db table
      var toPostAOIPos = {
        userID: this.$store.getters.getUID,
        qID: this.$store.state.route.params.queryID,
        leftPosition: leftPos,
        rightPosition: rightPos,
        topAOIPos1: topPos1,
        botAOIPos1: bottomPos1,
        topAOIPos2: topPos2,
        botAOIPos2: bottomPos2,
        topAOIPos3: topPos3,
        botAOIPos3: bottomPos3,
        topAOIPos4: topPos4,
        botAOIPos4: bottomPos4,
        topAOIPos5: topPos5,
        botAOIPos5: bottomPos5,
        topAOIPos6: topPos6,
        botAOIPos6: bottomPos6
      }
      await QueryService.userAOIPositions(toPostAOIPos)
      // stores resepective data into usergaze db table
      var dataArrayToString = JSON.stringify(dataArray)
      var toPostUserGaze = {
        userID: this.$store.getters.getUID,
        qID: this.$store.state.route.params.queryID,
        gazePoints: dataArrayToString
      }
      console.log(toPostUserGaze)
      await QueryService.userGaze(toPostUserGaze)

      var qID = parseInt(this.$store.state.route.params.queryID) + 1
      // this.clicked = [null, null, null, null, null, null]
      // console.log(this.clicked)
      if (qID < 31) {
        this.$store.dispatch('setqID', qID)
        this.$router.push(`/query/${qID}`)
      } else {
        this.$router.push('/questionnaire/3')
      }
    }
  }
  // beforeMount () {
  //   this.getAOI()
  // }
}
</script>

<style scoped>
  .resultPage {
    padding-left: 0px;
    max-width: 100%;
  }
  .flex.xs4 {
    max-width: 100%;
    margin-left: 50px;
  }
  .d-flex.offset-xs4 {
    margin-left: 50px;
    padding-left: 0px;
  }
  .container {
    text-align: center;
  }
  ul {
    list-style-type: none;
    max-width: 100%;
  }
  li {
    margin-bottom: 18px;
    max-width: 100%;
  }
  div {
    text-align: left
  }
  div.snip {
    word-wrap: break-word;
    overflow: hidden;
    height: 40px;
  }
  div.url {
    color: green;
    white-space: nowrap;
    width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: 16px
  }
  div.title {
    color: blue;
    width: 100%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: 20px
  }
  div.myButton {
    max-height: 48px;
  }
  @media only screen and (max-width: 1160px) {
    .flex.offset-xs4 {
      margin-left: 5px;
      margin-top: 55px;
    }
  }
</style>
