function SuggestedUsers({ users }) {
    return (
        <section className="flex flex-col gap-10 w-full h-full rounded-lg">
            <h1>Suggested Users</h1>

            <ul className="flex flex-col gap-10 w-full h-full">
                {users.map(user => (
                    <li className="flex flex-row gap-10 w-full h-full">
                        <img src={user.profilePic} alt="" className="w-[50px] h-[50px] rounded-full border-black border" />
                        <div>
                            <h1> {user.fullName} </h1>
                            <p>@{user.username}</p>
                        </div>
                    </li>
                ))}
            </ul>
        </section>
    )
}

export default SuggestedUsers