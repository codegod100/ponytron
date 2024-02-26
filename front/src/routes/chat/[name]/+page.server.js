import { get_chat, submit_chat, storedname, following } from "$lib/common";
export async function load({ params, cookies }) {
	let username = cookies.get("username")
	let chat = await get_chat(params.name)
	let friends = await following(username);
	return { friends, chat }
}