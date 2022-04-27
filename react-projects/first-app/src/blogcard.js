import React from 'react';

const  BlogCard = (properties) => {
    console.log(properties)
    return(
        <div className="card">
            <h3>{properties.name}</h3>
            <p>{properties.description}</p>
        </div>
    )
}

export default BlogCard;