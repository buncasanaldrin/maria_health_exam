import axios from 'axios'
import qs from 'qs'

// CONSTANTS
const API = {
  Drugs: {
    FETCH: 'https://api.fda.gov/drug/label.json/'
  }
}

// ACTIONS
export default {
  fetchDrugs({ commit }, params = []) {
    commit('setFetchedDrugs', { status: 'PENDING' })
    return axios.get(API.Drugs.FETCH, {
      params: params,
      paramsSerializer: function(params) {
        return qs.stringify(params, { encode: false })
      }
    }).then((res) => {
        commit('setFetchedDrugs', {
          status: 'FULFILLED',
          res: res.data,
          statusCode: res.status
        })
      })
      .catch((e) => {
        commit('setFetchedDrugs', {
          status: 'REJECTED',
          res: e.response.data,
          statusCode: e.response.status
        })
      })
  }
}
