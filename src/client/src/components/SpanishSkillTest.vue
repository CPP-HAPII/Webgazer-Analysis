<template>
  <v-container fluid grid-list-xl>
    <v-layout row align-left>
      <v-flex xs12 d-flex>
        <v-subheader>Spanish Skills Test</v-subheader>
      </v-flex>
    </v-layout>
    <v-form ref="spanishtest" v-model="valid">
      <v-layout row align-left>
          <ol>
            <li>
              <p>Al oír del accidente de su buen amigo, Paco se puso <select v-model="Q1">
              <option disabled value=""></option>
              <option value="AAAAA0">alegre</option>
              <option value="AAAAB0">fatigado</option>
              <option value="AAAAC0">hambriento</option>
              <option value="AAAAD1">desconsolado</option>
              </select>.</p>
            </li>
            <li>
              <p>No puedo comprarlo porque me <select v-model="Q2">
              <option disabled value=""></option>
              <option value="AAAAE1">falta</option>
              <option value="AAAAF0">dan</option>
              <option value="AAAAG0">presta</option>
              <option value="AAAAH0">regalan</option>
              </select> dinero.</p>
            </li>
            <li>
              <p>Tuvo que guardar cama por estar <select v-model="Q3">
              <option disabled value=""></option>
              <option value="AAAAI1">enfermo</option>
              <option value="AAAAJ0">vestido</option>
              <option value="AAAAK0">ocupado</option>
              <option value="AAAAL0">parado</option>
              </select>.</p>
            </li>
            <li>
              <p>Aquí está tu café, Juanito. No te quemes, que está muy <select v-model="Q4">
              <option disabled value=""></option>
              <option value="AAAAM0">dulce</option>
              <option value="AAAAN0">amargo</option>
              <option value="AAAAO0">agrio</option>
              <option value="AAAAP1">caliente</option>
              </select>.</p>
            </li>
            <li>
              <p>Al romper los anteojos, Juan se asustó porque no podía <select v-model="Q5">
              <option disabled value=""></option>
              <option value="AAAAQ0">discurrir</option>
              <option value="AAAAR0">oir</option>
              <option value="AAAAS1">ver</option>
              <option value="AAAAT0">entender</option>
              </select> sin ellos.</p>
            </li>
            <li>
              <p>¡Pobrecita! Está resfriada y no puede <select v-model="Q6">
              <option disabled value=""></option>
              <option value="AAAAU1">salir de casa</option>
              <option value="AAAAV0">recibir cartas</option>
              <option value="AAAAW0">respirar con pena</option>
              <option value="AAAAX0">leer las noticias</option>
              </select>.</p>
            </li>
            <li>
              <p>Era una noche oscura sin <select v-model="Q7">
              <option disabled value=""></option>
              <option value="AAAAY1">estrellas</option>
              <option value="AAAAZ0">camas</option>
              <option value="AAABA0">lágrimas</option>
              <option value="AAACA0">nubes</option>
              </select>.</p>
            </li>
            <li>
              <p>Cuando don Carlos salió de su casa, saludó a un amigo suyo: -Buenos días, <select v-model="Q8">
              <option disabled value=""></option>
              <option value="AAADA0">¿Qué va?</option>
              <option value="AAAEA0">¿Cómo es?</option>
              <option value="AAAFA0">¿Quién es?</option>
              <option value="AAAGA1">¿Qué tal?</option>
              </select>.</p>
            </li>
            <li>
              <p>¡Qué ruido había con los gritos de los niños y el <select v-model="Q9">
              <option disabled value=""></option>
              <option value="AAAHA0">olor</option>
              <option value="AAAIA0">sueño</option>
              <option value="AAAJA0">hambre</option>
              <option value="AAAKA1">ladrar</option>
              </select> de los perros!</p>
            </li>
            <li>
              <p>Para saber la hora, don Juan miró el <select v-model="Q10">
              <option disabled value=""></option>
              <option value="AAALA0">calendario</option>
              <option value="AAAMA0">bolsillo</option>
              <option value="AAANA0">estante</option>
              <option value="AAAOA1">despertador</option>
              </select>.</p>
            </li>
            <li>
              <p>Yo, que comprendo poco de mecánica, sé que el auto no puede funcionar sin <select v-model="Q11">
              <option disabled value=""></option>
              <option value="AAAPA0">permiso</option>
              <option value="AAAQA0">comer</option>
              <option value="AAARA1">aceite</option>
              <option value="AAASA0">bocina</option>
              </select>.</p>
            </li>
            <li>
              <p>Nos dijo mamá que era hora de comer y por eso <select v-model="Q12">
              <option disabled value=""></option>
              <option value="AAATA0">fuimos a nadar</option>
              <option value="AAAUA1">tomamos asiento</option>
              <option value="AAAVA0">comenzamos a fumar</option>
              <option value="AAAWA0">nos acostamos pronto</option>
              </select>.</p>
            </li>
            <li>
              <p>¡Cuidado con ese cuchillo o vas a <select v-model="Q13">
              <option disabled value=""></option>
              <option value="AAAXA1">cortate</option>
              <option value="AAAYA0">torcerte</option>
              <option value="AAAZA0">comerte</option>
              <option value="AABAA0">quemarte</option>
              </select> el dedo!</p>
            </li>
            <li>
              <p>Tuvo tanto miedo de caerse que se negó a <select v-model="Q14">
              <option disabled value=""></option>
              <option value="AACAA0">almorzar</option>
              <option value="AADAA0">charlar</option>
              <option value="AAEAA0">cantar</option>
              <option value="AAFAA1">patinar</option>
              </select> con nosotros.</p>
            </li>
            <li>
              <p>Abrió la ventana y miró: en efecto, grandes lenguas de <select v-model="Q15">
              <option disabled value=""></option>
              <option value="AAGAA0">zorrors</option>
              <option value="AAHAA0">serpientes</option>
              <option value="AAIAA0">cuero</option>
              <option value="AAJAA1">fuego</option>
              </select> salían llameando de las casas.</p>
            </li>
            <li>
              <p>Compró ejemplares de todos los diarios pero en vano. No halló <select v-model="Q16">
              <option disabled value=""></option>
              <option value="AAKAA0">los diez centavos</option>
              <option value="AALAA0">el periódico perdido</option>
              <option value="AAMAA1">la noticia que deseaba</option>
              <option value="AANAA0">los ejemplos</option>
              </select>.</p>
            </li>
            <li>
              <p>Por varias semanas acudieron colegas del difunto profesor a <select v-model="Q17">
              <option disabled value=""></option>
              <option value="AAOAA1">aliviar</option>
              <option value="AAPAA0">dulcificar</option>
              <option value="AAQAA0">embromar</option>
              <option value="AARAA0">estorbar</option>
              </select> el dolor de la viuda.</p>
            </li>
            <li>
              <p>Sus amigos pudieron haberlo salvado pero lo dejaron <select v-model="Q18">
              <option disabled value=""></option>
              <option value="AASAA0">ganar</option>
              <option value="AATAA0">parecer</option>
              <option value="AAUAA1">perecer</option>
              <option value="AAVAA0">acabar</option>
              </select>.</p>
            </li>
            <li>
              <p>Al salir de la misa me sentía tan caritativo que no pude menos que <select v-model="Q19">
              <option disabled value=""></option>
              <option value="AAWAA0">pegarle</option>
              <option value="AAXAA1">darle una limosna</option>
              <option value="AAYAA0">echar una mirada</option>
              <option value="AAZAA0">maldecir</option>
              </select> un pobre mendigo que había allí sentando.</p>
            </li>
            <li>
              <p>Al lado de la Plaza de Armas había dos limosneros pidiendo <select v-model="Q20">
              <option disabled value=""></option>
              <option value="ABAAA0">pedazos</option>
              <option value="ACAAA0">paz</option>
              <option value="ADAAA1">monedas</option>
              <option value="AEAAA0">escopetas</option>
            </select>.</p>
            </li>
            <li>
              <p>Siempre maltratado por los niños, el perro no podía acostumbrarse a <select v-model="Q21">
              <option disabled value=""></option>
              <option value="AFAAA1">las caricias</option>
              <option value="AGAAA0">los engaños</option>
              <option value="AHAAA0">las locuras</option>
              <option value="AIAAA0">los golpes</option>
              </select> de sus nuevos amos.</p>
            </li>
            <li>
              <p>¿Dónde estará mi cartera? La dejé aquí mismo hace poco y parece que el necio de mi hermano ha vuelto a <select v-model="Q22">
              <option disabled value=""></option>
              <option value="AJAAA0">dejármela</option>
              <option value="AKAAA0">deshacérmela</option>
              <option value="ALAAA1">escondérmela</option>
              <option value="AMAAA0">acabármela</option>
              </select>.</p>
            </li>
            <li>
              <p>Permaneció un gran rato abstraído, los ojos clavados en el fogón y el pensamiento <select v-model="Q23">
              <option disabled value=""></option>
              <option value="ANAAA0">en el bolsillo</option>
              <option value="AOAAA0">en el fuego</option>
              <option value="APAAA0">lleno de alboroto</option>
              <option value="AQAAA1">Dios sabe dónde</option>
              </select>.</p>
            </li>
            <li>
              <p>En vez de dirigir el tráfico estabas charlando, así que tú mismo <select v-model="Q24">
              <option disabled value=""></option>
              <option value="ARAAA0">sabes la gravedad</option>
              <option value="ASAAA0">eres testigo</option>
              <option value="ATAAA1">tuviste la culpa</option>
              <option value="AUAAA0">conociste a las victimas</option>
              </select> del choque.</p>
            </li>
            <li>
              <p>Posee esta tierra un clima tan propio para la agricultura como para <select v-model="Q25">
              <option disabled value=""></option>
              <option value="AVAAA0">la construccion de trampas</option>
              <option value="AWAAA0">el fomento de motines</option>
              <option value="AXAAA0">el costo de vida</option>
              <option value="AYAAA1">la cría de reses</option>
              </select>.</p>
            </li>
            <li>
              <p>Aficionado leal de obras teatrales, Juan se entristeció al saber <select v-model="Q26">
              <option disabled value=""></option>
              <option value="AZAAA1">del fallecimiento</option>
              <option value="BAAAA0">del éxito</option>
              <option value="CAAAA0">de la buena suerte</option>
              <option value="DAAAA0">de la alabanza</option>
              </select> del gran actor.</p>
            </li>
            <li>
              <p>Se reunieron a menudo para efectuar un tratado pero no pudieron <select v-model="Q27">
              <option disabled value=""></option>
              <option value="EAAAA0">desavenirse</option>
              <option value="FAAAA0">echarlo a un lado</option>
              <option value="GAAAA0">rechazarlo</option>
              <option value="HAAAA1">llevarlo a cabo</option>
              </select>.</p>
            </li>
            <li>
              <p>Se negaron a embarcarse porque tenían miedo de <select v-model="Q28">
              <option disabled value=""></option>
              <option value="IAAAA0">los peces</option>
              <option value="JAAAA1">los naufragios</option>
              <option value="KAAAA0">los faros</option>
              <option value="LAAAA0">las playas</option>
              </select>.</p>
            </li>
            <li>
              <p>La mujer no aprobó el cambio de domicilio pues no le gustaba <select v-model="Q29">
              <option disabled value=""></option>
              <option value="MAAAA0">el callejeo</option>
              <option value="NAAAA0">el puente</option>
              <option value="OAAAA0">esa estación</option>
              <option value="PAAAA1">aquel barrio</option>
              </select>.</p>
            </li>
            <li>
              <p>La mujer no aprobó el cambio de domicilio pues no le gustaba <select v-model="Q30">
              <option disabled value=""></option>
              <option value="QAAAA0">hojearlo</option>
              <option value="RAAAA0">ponérselo</option>
              <option value="SAAAA0">conservarlo</option>
              <option value="TAAAA1">repartirlo</option>
              </select>.</p>
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
