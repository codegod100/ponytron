import { get_users } from "$lib/common";

/** @type {import('./$types').PageServerLoad} */
export async function load({ params }) {
    let users = await get_users()
    return {
        users
    };
}