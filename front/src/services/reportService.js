import { api } from '@/plugins/api.plugin'

export default {
	save(data) {
		return api.post({
			url: `/save`,
			data: data
		})
	},

	getById(id) {
		return api.get({
			url: `/${id}`
		})
	},
}
