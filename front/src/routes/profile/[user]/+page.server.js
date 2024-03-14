import { get_user, following, get_statuses } from "$lib/common";
export async function load({ params, cookies }) {
    let jwt = cookies.get("jwt")
    let username = cookies.get("username")
    let user = await get_user(params["user"])
    let friends = await following(username);
    let statuses = await get_statuses({ user: params["user"], jwt })
    console.log({ friends })
    return { user, friends, statuses }
}