<template>
  <v-container
    id="user-profile"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        md="8"
      >
        <base-material-card
          color="secondary darken-4"
        >
          <template v-slot:heading>
            <div
              id="firstdiv"
              shaped
              class="displaynms font-weight-medium"
            >
              <v-chip
                medium
                dark
                color="secondary darken-3"
                outline
              >
                DEFAULT / PRESET VALUES
              </v-chip>
              <br>
              <ul>
                <li>
                  Initial Token Supply: &nbsp; 100,000,000<br>
                </li>
                <li>
                  Inflation begins in how many intervals? &nbsp; 24 = 2 yrs
                  <br>
                </li>
                <li>
                  Inflation tokens per 12 intervals? &nbsp;5,000,000 /12 (416,666.66) <br>
                </li>
                <li>
                  Inflation is turned off at: &emsp;&emsp; 210,000,000<br>
                </li>
                <li>
                  De-inflation ratio: &emsp;&emsp; 0.004 ( 0.01 = 1% )  <br><br>
                </li>
              </ul>
              <v-chip
                color="info lighten-2"
                medium
                raised
              >
                Inflation and de-inflation begin at the same time
              </v-chip>
            </div>
          </template>
          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="12"
                  md="4"
                >
                  <!-- class="inputc"  -->
                  <v-text-field
                    id="in-supply"
                    v-model="insupp"
                    class="purple-input display-2"
                    label="Initial Supply textfield"
                    type="string"
                    name="initial_supply_y"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  cols="12"
                  md="4"
                >
                  <validation-provider
                    v-slot="{ errors }"
                    ref="name"
                    name="name"
                    rules="required|alpha"
                  >
                    <v-text-field
                      v-model="name"
                      label="Name"
                    />
                    <span>{{ errors }}</span>
                  </validation-provider>

                  <v-text-field
                    id="aninflate"
                    v-model="number"
                    name="annual_inflation"
                    class="purple-input display-2"
                    type="number"
                    value="5000000"
                    label="Inflation per 12 intervals inputfield"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <!-- class="inputc"  -->
                  <v-text-field
                    label="Inflation begins in how many intervals:"
                    class="purple-input display-2"
                    value="24"
                    type="number"
                    name="start_inflation"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Inflation stops at:"
                    class="purple-input display-2"
                    value="210000000"
                    type="number"
                    name="stop_inflation_y"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    label="Disinflation ratio ( .01 = 1% ):"
                    class="purple-input display-2"
                    value="0.004"
                    type="number"
                    name="deratio"
                  />
                </v-col>
                <v-col
                  cols="12"
                  md="4"
                >
                  <v-btn
                    type="submit"
                    color="warning"
                    :disabled="invalid"
                  >
                    Submit
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </base-material-card>
      </v-col>
      <v-col
        cols="12"
        md="4"
      >
        <base-material-card
          class="v-card-profile"
          avatar="http://westteam.nulstar.com/nms/artws/Social_Telegram_G.svg"
        >
          <v-row>
            <v-col
              cols="12"
              md="4"
            >
              <v-card-text class="text-center">
                <h6 class="display-2 mb-1 grey--text">
                  Tryout Values
                </h6>

                <h4
                  class="display-2 font-weight-light mb-3 black--text"
                  :value="dataone"
                />

                <p
                  class="font-weight-light grey--text"
                  :value="dataoneb"
                />

                <p
                  class="font-weight-light grey--text"
                  :value="datatwo + datathree"
                />

                <v-btn
                  color="success"
                  rounded
                  class="mr-0"
                >
                  Continue
                </v-btn>
              </v-card-text>
            </v-col>
          </v-row>
        </base-material-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="8"
      >
        <base-material-card
          color="secondary darken-1"
        >
          <validation-observer
            v-slot="{ invalid }"
            ref="form"
          >
            <form
              name="form"
              @submit.prevent="onSubmit"
            >
              <v-row>
                <v-col
                  cols="12"
                  md="4"
                >
                  <validation-provider
                    v-slot="{ errors }"
                    name="E-mail"
                    rules="required|email"
                  >
                    <v-text-field
                      id="one1"
                      v-model="email"
                      name="E-mail"
                      type="email"
                      color="primary"
                      enabled="true"
                      outlined="true"
                      large
                      label="Email"
                      :messages="['Enter Email']"
                      :success="success"
                      :success-messages="successMsg"
                      :error="error"
                      :error-messages="errorMsg"
                      :error-count="errorCount"
                      hint="real email with @"
                      :persistent-hint="persistentHint"
                    />
                    <span>{{ errors[0] }}</span>
                  </validation-provider>
                </v-col>
                <v-col
                  cols="12"
                  md="4"
                >
                  <validation-provider
                    v-slot="{ errors }"
                    name="Inflation Top"
                    rules="required|numeric|min|max"
                  >
                    <v-text-field
                      v-model="inflationTop"
                      type="number"
                      min="300000"
                      max="999999999"
                      outlined="true"
                      color="primary"
                      enabled="true"
                      large
                      label="Inflation Stops at"
                      :messages="['Enter Amount']"
                      :success="success"
                      :success-messages="successMsg"
                      :error="error"
                      :error-messages="errorMsg"
                      :error-count="errorCount"
                      hint="Max 900,000,000"
                      :persistent-hint="persistentHint"
                    />
                    <span>{{ errors[0] }}</span>
                  </validation-provider>
                </v-col>
                <v-col
                  cols="12"
                  md="4"
                >
                  <validation-provider
                    v-slot="{ errors }"
                    name="Last Name"
                    rules="required|alpha"
                  >
                    <v-text-field
                      v-model="lastName"
                      type="text"
                      outline
                    />
                    <span>{{ errors[0] }}</span>
                  </validation-provider>
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <button
                    type="submit"
                    :disabled="invalid"
                    primary
                  >
                    Submit
                  </button>
                </v-col>
              </v-row>
            </form>
          </validation-observer>
        </base-material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  import { ValidationObserver, ValidationProvider, extend } from 'vee-validate'
  import { required, min, max, numeric } from 'vee-validate/dist/rules'
  import { mdiAccount } from 'material-icons'

  const givenNumber = 100000000
  const inSupply = givenNumber.toLocaleString('en-US')
  extend('required', {
    ...required,
    message: 'This field is required',
  })

  export default {
    min,
    max,
    numeric,
    mdiAccount,
    components: {
      ValidationProvider: ValidationProvider,
      ValidationObserver: ValidationObserver,
    },
    data: () => ({
      givenNumber,
      inSupply,
      email: '',
      inflationTop: '',
      lastName: '',
      dataone: 'Try different values and view a plot of how they play out over time.',
      dataoneb: 'Intervals can be thought of as months or 30/day increments.',
      datatwo: 'For this blockchain, the following values are set: ',
      datathree: 'Initial Supply:  100,000,000 VKG/NULS',
      datafour: 'Inflation begins in intervals: &emsp;&emsp; 24 (2 years)',
      datafive: 'Inflation tokens per 12 intervals: &emsp;&emsp; 5,000,000 / 12 (416,666.66) VKG/NULS',
      datasix: 'Inflation is turned off when inflation reaches:   210,000,000  VKG/NULS',
      dataseven: 'Disinflation ratio is:   0.004       ( 0.01 = 1% ) ',
      dataeight: 'Inflation and disinflation begin at the same time.',
      text: '',
      success: false,
      error: false,
      hideDetails: false,
      errorCount: 1,
      persistentHint: true,
    }),
    computed: {
      successMsg () {
        return this.success ? ['Done'] : []
      },
      errorMsg () {
        return this.error ? ['Error', 'Another one', 'One more', 'All the errors'] : []
      },
    },
    methods: {
      onSubmit () {
        alert('Form has been submitted!')
      },
      appendIconCallback () {
        alert('click:append')
      },
      prependIconCallback () {
        alert('click:prepend')
      },
    },
  }
</script>

<style>
  .displaynms {
    line-height: 1.7em;
    font-size: 24px!important;
    padding-left: 26px!important;
  }
  .v-chip {
    padding: 19px;
    margin-bottom: 10px!important;
  }
  .v-chip__content {
    font-size: 22px;
    font-weight: 400;
    padding-left: 22px;
    padding-right: 22px;
    padding-bottom: 14px;
    padding-top: 14px;
}
  .v-card__title {
    font-size: 22px;
    font-weight: 400;
    padding-top: 12px;
    padding-bottom: 14px;
    padding-left: 22px;
    margin-right: 22px;
    text-align: center;
}
</style>
