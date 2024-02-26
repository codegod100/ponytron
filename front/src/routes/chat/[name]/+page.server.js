import { get_chat, submit_chat, storedname } from "$lib/common";
/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
	console.log("reloading", params)
	let chat = await get_chat(params.name)
	return {
		chat

	};
}