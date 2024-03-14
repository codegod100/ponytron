import { get_users, create_user, login } from "$lib/common";
import { fail, redirect } from '@sveltejs/kit';

/** @type {import('./$types').PageServerLoad} */
export async function load({ params, route, url, cookies }) {
    console.log("page-server", url.pathname)
    let path = cookies.get("path")
    let username = cookies.get("username")
    if (path && username) {
        console.log({ path, username })
        cookies.set("path", "", { path: "/" })
        redirect(302, path)
    }
    let users = await get_users()
    return {
        users, nav: "main"
    };
}

export const actions = {
    default: async ({ cookies, request }) => {
        const data = await request.formData();
        let username = data.get("username")
        let password = data.get("password")
        cookies.set("username", username, { path: "/" })
        if (username) {
            let jwt
            await create_user({ username, password })
            console.log("doing jwt")
            try {
                jwt = await login({ username, password })
                console.log({ jwt })
            } catch {
                cookies.delete("username", { path: "/" })
                console.log("failing")
                return fail(400, { username, incorrect: true });
            }
            cookies.set("jwt", jwt, { path: "/" })
        }
    }
};