<script>
    import { get_users } from "$lib/common";
</script>

<div>Users:</div>
{#await get_users()}
    Grabbing users
{:then users}
    {#each users as user}
        <div>
            Username: {user.username}
        </div>
    {/each}
{/await}
