export async function load({ cookies }) {
    let username = cookies.get("username")
    console.log("username", username)
    return { username }
}

