import { useEffect, useState } from "react";
import { useLocation, useNavigate, useParams } from "react-router-dom";

export default function Product() {
    // const {id} = useParams();
    // const [product, setProduct] = useState()    
    
    const location = useLocation();
    const product = location.state


    // useEffect(() => {
    //     fetch(`https://fakestoreapi.com/products/${id}`)
    //     .then((res) => res.json())
    //     .then((prods) => setProduct(prods))
    //     .catch((err) => console.log(err))
    //   }, [])

  return (
    <div>        
      {
        product ? (
            <>
            <p> {product.title} </p>
            <p> {product.price} </p>
            <p> {product.description} </p>
            </>
        ) : <p>There is nothing</p>
      }
    </div>
  );
}