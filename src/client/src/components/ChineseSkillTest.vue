<template>
  <v-container fluid grid-list-xl>
    <v-layout row align-left>
      <v-flex xs12 d-flex>
        <v-subheader>Chinese Skills Test</v-subheader>
      </v-flex>
    </v-layout>
    <v-form ref="chinesetest" v-model="valid">
      <v-layout row align-left>
          <ol>
            <p>第 1-5 题：选词填空。</p>
            <p>A) 随着 B) 尝 C) 春节 D) 坚持 E) 收拾 F) 提醒</p>
            <p>例如：她每天都（ D ）走路上下班，所以身体一直很不错。</p>
            <li>
              <p>虽然现在离（<select v-model="Q1">
              <option disabled value=""></option>
              <option value="AAAAA0">A</option>
              <option value="AAAAB0">B</option>
              <option value="AAAAC1">C</option>
              <option value="AAAAD0">D</option>
              <option value="BAAAD0">E</option>
              <option value="CAAAD0">F</option>
              </select>）还有段时间，但是不少人已经开始准备过年的东西了。</p>
            </li>
            <li>
              <p>研究证明，人们的心情会（<select v-model="Q2">
              <option disabled value=""></option>
              <option value="AAAAE1">A</option>
              <option value="AAAAF0">B</option>
              <option value="AAAAG0">C</option>
              <option value="AAAAH0">D</option>
              <option value="BAAAH0">E</option>
              <option value="CAAAH0">F</option>
              </select>）天气的变化而变化。</p>
            </li>
            <li>
              <p>明天可能下雨，你记得（<select v-model="Q3">
              <option disabled value=""></option>
              <option value="AAAAI0">A</option>
              <option value="AAAAJ0">B</option>
              <option value="AAAAK0">C</option>
              <option value="AAAAL0">D</option>
              <option value="BAAAL0">E</option>
              <option value="CAAAL1">F</option>
              </select>）儿子带雨伞。</p>
            </li>
            <li>
              <p>这是你做的饺子？真香！我先（<select v-model="Q4">
              <option disabled value=""></option>
              <option value="AAAAM0">A</option>
              <option value="AAAAN1">B</option>
              <option value="AAAAO0">C</option>
              <option value="AAAAP0">D</option>
              <option value="BAAAP0">E</option>
              <option value="CAAAP0">E</option>
              </select>）一个。</p>
            </li>
            <li>
              <p>快把房间（<select v-model="Q5">
              <option disabled value=""></option>
              <option value="AAAAQ0">A</option>
              <option value="AAAAR0">B</option>
              <option value="AAAAS0">C</option>
              <option value="AAAAT0">D</option>
              <option value="BAAAT1">E</option>
              <option value="CAAAT0">E</option>
              </select>）一下，准备一些水果，一会儿有客人要来。</p>
            </li>
            <p>第 6-10 题：选词填空。</p>
            <p>A) 反映 B) 陪 C) 温度 D) 堵车 E) 来得及 F) 肯定</p>
            <p>例如：A：今天真冷啊，好像白天最高（ C ）才 2℃。</p>
            <p>B：刚才电视里说明天更冷。</p>
            <li>
              <p>A：这些瓶子的数量对吧？</p>
              <p>B：我都仔细检查过了，（<select v-model="Q6">
              <option disabled value=""></option>
              <option value="AAAAU0">A</option>
              <option value="AAAAV0">B</option>
              <option value="AAAAW0">C</option>
              <option value="AAAAX0">D</option>
              <option value="BAAAX0">E</option>
              <option value="CAAAX1">F</option>
              </select>）没问题。</p>
            </li>
            <li>
              <p>A：讨论会开得顺利吗？</p>
              <p>B：顺利，大家（<select v-model="Q7">
              <option disabled value=""></option>
              <option value="AAAAY1">A</option>
              <option value="AAAAZ0">B</option>
              <option value="AAABA0">C</option>
              <option value="AAACA0">D</option>
              <option value="BAACA0">E</option>
              <option value="CAACA0">F</option>
              </select>）了不少管理过程中出现的问题，对下一步工作 很有帮助。</p>
            </li>
            <li>
              <p>A：火车快开了，他怎么还没来？</p>
              <p>B：他一般很准时的，可能是路上（<select v-model="Q8">
              <option disabled value=""></option>
              <option value="AAADA0">A</option>
              <option value="AAAEA0">B</option>
              <option value="AAAFA0">C</option>
              <option value="AAAGA1">D</option>
              <option value="BAAGA0">E</option>
              <option value="CAAGA0">F</option>
              </select>），别着急，再等等。</p>
            </li>
            <li>
              <p>A：快点儿，今天千万不能迟到。</p>
              <p>B：还有 10 分钟呢，（<select v-model="Q9">
              <option disabled value=""></option>
              <option value="AAAHA0">A</option>
              <option value="AAAIA0">B</option>
              <option value="AAAJA0">C</option>
              <option value="AAAKA0">D</option>
              <option value="BAAKA1">E</option>
              <option value="CAAKA0">F</option>
              </select>）。</p>
            </li>
            <li>
              <p>A：我（<select v-model="Q10">
              <option disabled value=""></option>
              <option value="AAALA0">A</option>
              <option value="AAAMA1">B</option>
              <option value="AAANA0">C</option>
              <option value="AAAOA0">D</option>
              <option value="BAAOA0">E</option>
              <option value="CAAOA0">F</option>
              </select>）你一起去吧，可以顺便活动活动。</p>
              <p>B：太好了，我们现在就出发</p>
            </li>
            <p>第 11-15 题：请选出正确答案。</p>
            <p>例如：她很活泼，说话很有趣，总能给我们带来快乐，我们都很喜欢和她在一 起。</p>
            <p>她是个什么样的人？<b>A) 幽默</b> B) 马虎 C) 骄傲 D) 害羞</p>
            <li>
              <p>怎样才能说一口流利的外语呢？如果你有一定的语言基础和经济条件，那 么出国是最好的选择。因为语言环境对学习语言有重要的作用。</p>
              <p>去国外学习外语是因为：<select v-model="Q11">
              <option disabled value=""></option>
              <option value="AAAPA1">语言环境好</option>
              <option value="AAAQA0">经济条件好</option>
              <option value="AAARA0">有语言基础</option>
              <option value="AAASA0">学习更认真</option>
              </select></p>
            </li>
            <li>
              <p>"生日快乐！" "祝爸爸生日快乐！" 晚上我刚回到家，妻子和儿子就一起祝 我生日快乐，并送给我生日礼物。这时我才明白过来，今天是我的生日。</p>
              <p>根据这段话，可以知道我：<select v-model="Q12">
              <option disabled value=""></option>
              <option value="AAATA0">加班了</option>
              <option value="AAAUA0">身体不舒服</option>
              <option value="AAAVA0">没按时回家</option>
              <option value="AAAWA1">忘记了生日</option>
              </select></p>
            </li>
            <li>
              <p>我是前天到北京的，想借这次机会去长城看看，可是公司的事情很多，时 间安排得 很紧张。</p>
              <p>我最可能来北京：<select v-model="Q13">
              <option disabled value=""></option>
              <option value="AAAXA0">旅游</option>
              <option value="AAAYA0">休息</option>
              <option value="AAAZA1">出差</option>
              <option value="AABAA0">请假</option>
              </select></p>
            </li>
            <li>
              <p>兴趣是最好的老师，如果孩子对一件事情感兴趣，那他一定会主动、努力 地去学习，效果也会更好。</p>
              <p>为了提高学习效果，应该让孩子：<select v-model="Q14">
              <option disabled value=""></option>
              <option value="AACAA0">积累经验</option>
              <option value="AADAA0">努力学习</option>
              <option value="AAEAA1">产生兴趣</option>
              <option value="AAFAA0">相信自己</option>
              </select></p>
            </li>
            <li>
              <p>有的时候，我们要学会拒绝别人。拒绝别人，要找到合适、礼貌的方法， 否则，如果表达不合适，就会引起误会。</p>
              <p>这段话主要说怎样：<select v-model="Q15">
              <option disabled value=""></option>
              <option value="AAGAA1">拒绝别人</option>
              <option value="AAHAA0">获得尊重</option>
              <option value="AAIAA0">减少误会</option>
              <option value="AAJAA0">获得原谅</option>
              </select></p>
            </li>
            <p>第 16-19 题：选词填空。</p>
            <li>
              <p>孩子一旦做错了事，总是会<select v-model="Q16">
              <option disabled value=""></option>
              <option value="AAKAA0">担忧</option>
              <option value="AALAA0">忧虑</option>
              <option value="AAMAA0">害怕</option>
              <option value="AANAA1">担心</option>
              </select>父母责备他，如果正如他所想的那样， 父母责备 了他，孩子反而会有一种“如释重负”的感觉，对批评和自己所犯 的过错也就<select v-model="Q17">
              <option disabled value=""></option>
              <option value="BANAA0">漠不关心</option>
              <option value="CANAA0">无所作为</option>
              <option value="DANAA0">不言而喻</option>
              <option value="EANAA1">不以为然</option>
              </select>了。相反，如果父母<select v-model="Q18">
              <option disabled value=""></option>
              <option value="FANAA0">维持</option>
              <option value="GANAA0">坚持</option>
              <option value="HANAA0">支持</option>
              <option value="IANAA1">保持</option>
              </select>沉默，孩子的心里反而 会<select v-model="Q19">
              <option disabled value=""></option>
              <option value="JANAA0">平静</option>
              <option value="KANAA0">慌张</option>
              <option value="LANAA0">谨慎</option>
              <option value="MANAA1">紧张</option>
              </select> ，会感到 "不自在"，进 而反思自己的错误。</p>
            </li>
            <li>
              <p>有这样一群人，他们<select v-model="Q20">
              <option disabled value=""></option>
              <option value="ABAAA0">愿意</option>
              <option value="ACAAA0">喜欢</option>
              <option value="ADAAA1">热爱</option>
              <option value="AEAAA0">追求</option>
              </select>工作，只要工作<select v-model="Q21">
              <option disabled value=""></option>
              <option value="BEAAA0">希望</option>
              <option value="CEAAA0">要求</option>
              <option value="DEAAA1">需要</option>
              <option value="EEAAA0">需求</option>
              </select>，他们就会变换住处，<select v-model="Q22">
              <option disabled value=""></option>
              <option value="FEAAA0">而且</option>
              <option value="GEAAA0">宁可</option>
              <option value="HEAAA1">甚至</option>
              <option value="IEAAA0">并且</option>
              </select>变换生活的城市，所以他们<select v-model="Q23">
              <option disabled value=""></option>
              <option value="JEAAA0">等待</option>
              <option value="KEAAA0">往往</option>
              <option value="LEAAA1">习惯</option>
              <option value="MEAAA0">频繁</option>
              </select>搬家。</p>
            </li>
            <li>
              <p>我们要学会<select v-model="Q24">
              <option disabled value=""></option>
              <option value="ARAAA0">支配</option>
              <option value="ASAAA1">控制</option>
              <option value="ATAAA0">限制</option>
              <option value="AUAAA0">掌握</option>
              </select> 自己的心情，而不是让别人决定你的心情，要<select v-model="Q25">
              <option disabled value=""></option>
              <option value="BTAAA0">减少</option>
              <option value="CTAAA1">加强</option>
              <option value="DTAAA0">增强</option>
              <option value="ETAAA0">减弱</option>
              </select> 自己 对别人坏情绪的 "免疫力"，只有这样才能每天<select v-model="Q26">
              <option disabled value=""></option>
              <option value="ETAAA0">得到</option>
              <option value="FTAAA1">拥有</option>
              <option value="GTAAA0">享受</option>
              <option value="HTAAA0">充满</option>
              </select> 一份好心情。</p>
            </li>
            <li>
              <p>一个姑娘和一个小伙子结婚了，他们结婚以后的生活十分幸福。小伙子非常 喜欢足球，每次电视中有足球比赛的时候，他连饭都不吃也要看。对此，年轻的 妻子一点儿<select v-model="Q27">
              <option disabled value=""></option>
              <option value="EAAAA1">办法</option>
              <option value="FAAAA0">意思</option>
              <option value="GAAAA0">方式</option>
              <option value="HAAAA0">能力</option>
              </select> 也没有。一天，电视里又播放足球比赛，丈夫坐在电视机前一动 也不动，妻子跟他说话他也 <select v-model="Q28">
              <option disabled value=""></option>
              <option value="IAAAA1">好像</option>
              <option value="JAAAA0">相似</option>
              <option value="KAAAA0">表示</option>
              <option value="LAAAA0">相同</option>
              </select> 没有听到。年轻的妻子非常 <select v-model="Q29">
              <option disabled value=""></option>
              <option value="MAAAA0">平静</option>
              <option value="NAAAA0">着急</option>
              <option value="OAAAA1">生气</option>
              <option value="PAAAA0">担心</option>
              </select> ，她哭着回到自 己的妈妈家，可是回 到家的时候却发现家里只有爸爸一个人，也坐在电视机前看 足球比赛。 "<select v-model="Q30">
              <option disabled value=""></option>
              <option value="QAAAA1">妈妈呢</option>
              <option value="RAAAA0">爸爸，你累了吧</option>
              <option value="SAAAA0">妈妈也看足球比赛</option>
              <option value="TAAAA0">您怎么不看电视呢</option>
              </select>？" 她很奇怪。"回她的妈妈家了。" 父亲头也不回地说。</p>
            </li>
          </ol>
      </v-layout>
      <v-layout row align-left>
        <v-flex xs4 d-flex>
          <v-btn v-on:click="Continue" :disabled="!valid">Next</v-btn>
        </v-flex>
      </v-layout>
    </v-form>
  </v-container>
</template>

<script>
import QueryService from '@/services/QueryService'
export default {
  data () {
    return {
      valid: true,
      score: null,
      Q1: null,
      Q2: null,
      Q3: null,
      Q4: null,
      Q5: null,
      Q6: null,
      Q7: null,
      Q8: null,
      Q9: null,
      Q10: null,
      Q11: null,
      Q12: null,
      Q13: null,
      Q14: null,
      Q15: null,
      Q16: null,
      Q17: null,
      Q18: null,
      Q19: null,
      Q20: null,
      Q21: null,
      Q22: null,
      Q23: null,
      Q24: null,
      Q25: null,
      Q26: null,
      Q27: null,
      Q28: null,
      Q29: null,
      Q30: null
    }
  },
  methods: {
    async Continue () {
      try {
        var skillLevel = parseInt(this.Q1.charAt(5)) + parseInt(this.Q2.charAt(5)) + parseInt(this.Q3.charAt(5)) + parseInt(this.Q4.charAt(5)) + parseInt(this.Q5.charAt(5)) + parseInt(this.Q6.charAt(5)) + parseInt(this.Q7.charAt(5)) + parseInt(this.Q8.charAt(5)) + parseInt(this.Q9.charAt(5)) + parseInt(this.Q10.charAt(5)) + parseInt(this.Q11.charAt(5)) + parseInt(this.Q12.charAt(5)) + parseInt(this.Q13.charAt(5)) + parseInt(this.Q14.charAt(5)) + parseInt(this.Q15.charAt(5)) + parseInt(this.Q16.charAt(5)) + parseInt(this.Q17.charAt(5)) + parseInt(this.Q18.charAt(5)) + parseInt(this.Q19.charAt(5)) + parseInt(this.Q20.charAt(5)) + parseInt(this.Q21.charAt(5)) + parseInt(this.Q22.charAt(5)) + parseInt(this.Q23.charAt(5)) + parseInt(this.Q24.charAt(5)) + parseInt(this.Q25.charAt(5)) + parseInt(this.Q26.charAt(5)) + parseInt(this.Q27.charAt(5)) + parseInt(this.Q28.charAt(5)) + parseInt(this.Q29.charAt(5)) + parseInt(this.Q30.charAt(5))
        var toPost = {
          userID: this.$store.getters.getUID,
          skill: skillLevel
        }
        var response = (await QueryService.testresult(toPost)).status

        if (response === 200) {
          console.log(skillLevel)
          await QueryService.pageUpdate({id: this.someId})
          this.$router.push('/query/1')
        }
      } catch (err) {
        alert('Please complete the test to move on')
      }
    }
  }
}
</script>

<style scoped>
  ol {
      align-content: "left";
      text-align: "left";
    }
  select {
    border-style: solid;
  }
</style>
