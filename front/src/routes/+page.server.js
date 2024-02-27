import { get_users, create_user, login } from "$lib/common";

/** @type {import('./$types').PageServerLoad} */
export async function load({ params }) {
    let users = await get_users()
    return {
        users
    };
}

export const actions = {
    default: async ({ cookies, request }) => {
        const data = await request.formData();
        let username = data.get("username")
        let password = data.get("password")
        let jwt = await login({ username, password })
        console.log({ jwt })
        cookies.set("username", username, { path: "/" })
        if (username) {
            await create_user({ username, password })
        }
        console.log("form data", data)
    }
};