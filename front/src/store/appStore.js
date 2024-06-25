import { defineStore } from 'pinia'

export const useLocaleStore = defineStore('localeStore', {
	state: () => ({
		locale: {}
	}),
	getters: {
		getLocale() {
			return this.locale
		},
		getIsoCode() {
			return this.locale.isoCode
		}
	},
	actions: {
		setLocale(locale) {
			this.locale = locale
		}
	}
})
