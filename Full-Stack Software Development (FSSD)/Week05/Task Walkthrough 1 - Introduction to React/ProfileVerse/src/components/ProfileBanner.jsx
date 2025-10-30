function ProfileBanner({ coverPhoto, profilePic, fullName, username, location }) {
    const containerStyling = {
        backgroundImage: `url(${coverPhoto})`,
    }

    return (
        <section className="w-full h-[40vh] flex rounded-lg" style={containerStyling}>
            {/* User details */}
            <div className="flex items-center gap-10 self-end m-10">
                {/* Profile image */}
                <img className="w-[150px] h-[150px] rounded-full border-black border " src={profilePic} alt="" />

                {/* User information */}
                <div>
                    <h1> {fullName} </h1>
                    <p>@{username}</p>

                    <p> {location} </p>
                </div>
            </div>
        </section>
    )
}

export default ProfileBanner;