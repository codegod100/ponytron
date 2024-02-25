import { PUBLIC_API } from "$env/static/public";
import { json } from "@sveltejs/kit";
import { persisted } from 'svelte-persisted-store'
let users_url = PUBLIC_API + "/users";
export let get_users = async () => {
    let req = fetch(users_url);
    return (await req).json();
};
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

export let storedname = persisted("username", "")


// let emojis = ["😀", "😍", "🤔", "🚀", "🏆", "🎉", "🤷‍♂️", "💃", "🤝", "🏁"]
// export let randomEmoji = () => emojis[Math.floor(Math.random() * emojis.length)];
