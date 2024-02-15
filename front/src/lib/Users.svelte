<script>
    import { PUBLIC_API } from "$env/static/public";
    let get_users = async () => {
        let users_url = PUBLIC_API + "/users";
        let req = fetch(users_url);
        return (await req).json();
    };
</script>

{PUBLIC_API}
<div>
    Users:
</div>
{#await get_users() then users}
    <div>
        {#each users as user}
            Username: {user.username}
        {/each}
    </div>
{/await}
