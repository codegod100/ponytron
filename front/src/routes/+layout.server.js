export async function load({ cookies }) {
    let username = cookies.get("username")
    let jwt = cookies.get("jwt")
    return { username, jwt }
}

