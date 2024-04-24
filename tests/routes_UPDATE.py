def test_update_product(self):
         """It should Update an existing Product"""
        # create a product to update
        test_product = ProductFactory()
        
        #send a self.client.post() request to the BASE_URL with a json payload of test_product.serialize()
        #assert that the resp.status_code is status.HTTP_201_CREATED
        # UPDATE THE PRODUCT
        # get the data from resp.get_json() as new_product
        # change new_account["description"] to unknown
        # send a self.client.put() request to the BASE_URL with a json payload of new_product
        # assert that the resp.status_code is status.HTTP_200_OK
        # get the data from resp.get_json() as updated_product
        # assert that the updated_product["description"] is whatever you changed it to
