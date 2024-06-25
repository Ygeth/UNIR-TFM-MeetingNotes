import axios from 'axios'
// 
// import { env } from '@/utils/environment.util'
export const METHODS = {
	GET: 'get',
	POST: 'post',
	PUT: 'put',
	DELETE: 'delete',
}

// console.log(env)

const baseConfigDTO = {
	baseURL: "http://localhost:7000/api",
	headers: { 'Content-Type': 'application/json' },
	useRequestInterceptor: true,
	useAuth: true,
}

export class ApiPlugin {
	constructor(config = baseConfigDTO) {
		this.config = config
		this.axios = axios.create({
			baseURL: this.config.baseURL,
			headers: this.config.headers,
		})
		this.interceptors()
	}

	get(config) {
		return this.request({ ...config, method: METHODS.GET })
	}

	post(config) {
		return this.request({ ...config, method: METHODS.POST })
	}

	put(config) {
		return this.request({ ...config, method: METHODS.PUT })
	}

	delete(config) {
		return this.request({ ...config, method: METHODS.DELETE })
	}

	request(config) {
		return this.axios(config)
	}

	interceptors() {
		if (this.config?.useRequestInterceptor) {
			// Auth token Config
			// this.axios.interceptors.request.use(
			// 	config => {
			// 		if (this.config.useAuth && this.auth)
			// 			config.headers.Authorization = `Bearer ${this.auth.getJwtToken()}`

			// 		return config
			// 	},
			// 	error => {
			// 		return Promise.reject(error)
			// 	}
			// )
		}

		this.axios.interceptors.response.use(
			response => response,
			error => {
				if (error.response.status === 401 || error.response.status === 403) {
					// window.location.href = environmentVariables.VUE_APP_CRM_LOGIN
					console.error('Unauthorized')
				}
				return Promise.reject(error)
			}
		)
	}
}

export const api = new ApiPlugin(baseConfigDTO)
