<template>
  <div>
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <base-material-card
          id="matcard"
          color="success"
          class="v-card-profile"
        >
          <span>
            Second Card starts here
          </span>
          <!--
          // <template v-show="tshowing">
          //   // <span> {{ vmodsel1 }} </span>
          //   // <span> {{ vmodsel2 }} </span>
          //   // <span> {{ vmodsel3 }} </span>
          //   // <span> {{ vmodsel4 }} </span>
          //   // <span> {{ vmodsel5 }} </span>
          // </template>
          -->
        </base-material-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  // import { vmodsel1, vmodsel2, vmodsel3, vmodsel4, vmodsel5 } from '@/views/dashboard/pages/UserProfile'
  export default {
    name: 'SecondCard',
    data: () => ({
      placehold: 'placeholder',
      tshowing: true,
      // vmodsel2,
      // vmodsel3,
      // vmodsel4,
      // vmodsel5,
    }),
  }
</script>
