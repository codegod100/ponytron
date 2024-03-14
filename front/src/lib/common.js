import { PUBLIC_API } from "$env/static/public";
import { json } from "@sveltejs/kit";

import { persisted } from 'svelte-persisted-store'
export let get_users = async () => {
    let users_url = PUBLIC_API + "/users";
    let req = fetch(users_url);
    return (await req).json();
};

export let get_user = async (username) => {
    let url = PUBLIC_API + `/user/${username}`
    let req = fetch(url);
    return (await req).json();
}
export let get_chat = async (name) => {
    let get_chat_url = PUBLIC_API + `/chat/${name}`
    let req = fetch(get_chat_url);
    return (await req).json();
}

export let get_chats = async () => {
    let url = PUBLIC_API + `/chats`
    let req = fetch(url);
    return (await req).json();
}

export let create_user = async (data) => {
    let create_user_url = PUBLIC_API + `/create_user`
    await fetch(create_user_url, {
        method: "POST",
        body: JSON.stringify(data)
    })
}

export let create_chat = async (data) => {
    let url = PUBLIC_API + `/chats`
    await fetch(url, {
        method: "POST",
        body: JSON.stringify(data)
    })
}
let submit_chat_url = PUBLIC_API + "/submit_chat"
export let submit_chat = async (data) => {
    let req = await fetch(submit_chat_url, {
        method: "POST",
        body: JSON.stringify(data)
    })
}

export let subscribe = async (data) => {
    let url = PUBLIC_API + "/subscribe"
    await fetch(url, {
        method: "POST",
        body: JSON.stringify(data)
    })
}

export let unsubscribe = async (data) => {
    let url = PUBLIC_API + "/unsubscribe"
    await fetch(url, {
        method: "POST",
        body: JSON.stringify(data)
    })
}

export let following = async (user) => {
    let url = PUBLIC_API + `/following/${user}`
    let req = await fetch(url)
    return (await req).json();
}

export let create_status = async (data) => {
    let url = PUBLIC_API + "/status"
    await fetch(url, {
        method: "POST",
        body: JSON.stringify(data)
    })
}

export let get_statuses = async (user) => {
    let url = PUBLIC_API + `/statuses/${user}`
    let req = await fetch(url)
    return (await req).json();
}

export let login = async (data) => {
    let url = PUBLIC_API + "/login"
    let req = await fetch(url, {
        method: "POST",
        body: JSON.stringify(data)
    })
    let t = await req.text()
    if (t == "false") {
        // return fail(400, { data, incorrect: true })
        throw new Error("Failed to authenticate")
    }
    console.log({ t })
    return t
}
export let storedname = persisted("username", "")


