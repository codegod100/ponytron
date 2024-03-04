import { get_chats } from "$lib/common";
import randomEmoji from '@alexfrankcodes/random-emoji'


/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
    console.log("reloading")
    let chats = await get_chats()
    let chat_names = chats.map((chat) => chat.name)
    console.log("names", chat_names)
    let emoji = randomEmoji.random()
    let tries = 0
    while (chat_names.includes(emoji) && tries < 100) {
        emoji = randomEmoji.random()
        console.log("moj", emoji)
        tries++
    }
    return {
        chats: await get_chats(),
        emoji,
        nav: "chats"

    };
}