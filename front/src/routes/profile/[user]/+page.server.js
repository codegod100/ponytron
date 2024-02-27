import { get_user, following } from "$lib/common";
export async function load({ params, cookies }) {
    let username = cookies.get("username")
    let user = await get_user(params["user"])
    let friends = await following(username);
    console.log({ friends })
    return { user, friends }
}