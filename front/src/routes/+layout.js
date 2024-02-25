let logged_in = false
import {get} from 'svelte/store'
import {storedname, create_user} from "$lib/common"
let username = get(storedname)

if(username){
    logged_in = true
}

/** @type {import('./$types').LayoutServerLoad} */
export function load({ params }) {
    console.log("server", username)
	return {username
		
	};
}