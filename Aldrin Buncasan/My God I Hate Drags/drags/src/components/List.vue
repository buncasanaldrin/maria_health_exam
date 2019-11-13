<template>
  <div class="container">
    <b-row>
      <b-col xl="12" lg="12" md="12">
        <h1>Drugs List </h1><hr>
        <form method="post" @submit.prevent="handleSearch" class="mt-4">
          <b-row>
            <b-form-group class="col-3" label="Generic Name">
              <b-form-input
                v-model="form.generic_name"
                placeholder="Enter Generic Name"
                name="search"
                type="text"
              />
              </b-form-group>
                <b-form-group class="col-3" label="Brand Name">
                  <b-form-input
                    v-model="form.brand_name"
                    placeholder="Enter Brand Name"
                    name="search"
                    type="text"
                  />
              </b-form-group>
                <b-form-group class="col-3" label="Route">
                  <b-form-select v-model="form.route" :options="routes_list"></b-form-select>
                </b-form-group>
                <b-form-group class="col-3" label="-">
                  <b-button :disabled="isBusy" type="submit" variant="info">
                    Search
                  </b-button>
                </b-form-group>
              </b-row>
          </form>
          <br>
          <transition name="fade">
          <div class="loading" v-show="loading">
            <span class="fa fa-spinner fa-spin"></span> loading...
          </div>
          </transition>
          <div class="list-group" id="infinite-list">
            <b-table head-variant='dark' striped :busy="isBusy" :items="items" :fields="fields" show-empty></b-table>
            <h1 class="text-center" :class="displaySet">No more products to display</h1>
          </div>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import RoutesMixin from '../mixins/routes.js'
export default {
  mixins: [RoutesMixin],
  data() {
    return {
      isBusy: false,
      query_search: '',
      previous_count: 0,
      form: {
        generic_name: '',
        brand_name: '',
        route: '',
      },
      items: [],
      fields: [],
      limit: 10,
      nextItem: 10,
      loading: false,
      displaySet: 'field-display-none'
    }
  },
  mounted () {
    // Detect when scrolled to bottom.
    const listElm = document.querySelector('#infinite-list')
    listElm.addEventListener('scroll', e => {
      if (e.isTrusted) {
        if(listElm.scrollTop + listElm.clientHeight >= listElm.scrollHeight) {
          this.loadMore()
        }
      }
    })
  },
  computed: {
    // Map or get getters from vuex store
    ...mapGetters([
      'fetchedDrugs',
    ]),
  },
  created() {
    // Fetch data on-load
    this.fetch({limit: this.limit})
  },
  methods: {
    // Map or get actions from vuex store
    ...mapActions([
      'fetchDrugs',
    ]),
    // Action for scrolling load more
    async loadMore () {
      this.loading = true
      this.previous_count = this.items.length
      this.limit = (this.nextItem + this.limit)

      this.fetch({
        limit: this.limit, 
        search: this.query_search
      })
    },
    handleSearch() {
          
      // Action for search
      this.isBusy = true
      this.query_search = ''
      for (var s in this.form) {
        if (this.form[s]) {
          if (this.query_search) this.query_search += '+AND+'
          this.query_search += 'openfda.' + s + ':' + this.form[s]
        }
      }

      this.fetch({
        limit: this.limit,
        search: this.query_search
      })
          
    },
    async fetch(params = {}) {

      // fetch method came from vuex store actions
      await this.fetchDrugs(params)
      // fetched results came from vuex store getters
      const fetched = this.fetchedDrugs

      // Loading state of table and while scrolling
      this.isBusy = false
      this.loading = false

      // If fetch is successful
      if (fetched.status === 'FULFILLED') {
        // Get value from 'res' key
        const { res } = fetched
        // Record Fields
        this.fields = [
          { key: 'openfda.generic_name[0]', label: 'Generic Name', tdClass: 'generic-name-row' },
          { key: 'openfda.brand_name[0]', label: 'Brand Name' },
          { key: 'openfda.product_type[0]', label: 'Product Type' },
          { key: 'openfda.route[0]', label: 'Route of Administration' },
          { key: 'indications_and_usage[0]', label: 'Indication and Usage' },
          { key: 'warnings[0]', label: 'Warnings', thStyle: { color: 'red' }, tdClass: 'warning-row' },
          { key: 'active_ingredient[0]', label: 'Active Ingredients' },
          { key: 'inactive_ingredient[0]', label: 'Inactive Ingredients' },
          { key: 'storage_and_handling[0]', label: 'Storage' },
        ]
        // Records
        this.items = res.results

        // If receives a FULFILLED status but nothing more to display
        if (this.items.length < this.limit) {
          this.displaySet = 'field-display-block'
        }
      } else {
          // If receives a NOT_FOUND status or no matches found
          if (fetched.res.error.code === 'NOT_FOUND') {
            this.items = []
          }
          // If receives a BAD_REQUEST status but nothing more to display
          if (fetched.res.error.code === 'BAD_REQUEST') {
            this.displaySet = 'field-display-block'
            this.limit = this.items.length
          }
      }
    }
  },
}
</script>
<style>
    body {
      font-family: Arial;
    }

    .generic-name-row {
      font-weight: bold;
    }

    .warning-row {
      color: red;
    }

    .container {
      padding: 40px 80px 15px 80px;
      background-color: #fff;
      border-radius: 8px;
      max-width: 1300px;
    }

    .list-group {
      overflow: auto;
      height: 70vh;
      border: 2px solid #dce4ec;
      border-radius: 5px;
    }

    .loading {
      background: #6495ED;
      text-align: center;
      position: absolute;
      color: #fff;
      z-index: 9;
      padding: 11px 70px;
      border-radius: 5px;
      left: calc(50% - 45px);
      top: calc(50% - 18px);
    }

    .field-display-none {
      display: none;
    }

    .field-display-block {
      display: block;
    }

</style>