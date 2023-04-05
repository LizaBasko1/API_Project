import os
from ProductAPI.files import GET_publish
from ProductAPI.base import Base
import json



class GetPublishMethods(Base):
    ACTIVITY_API_WITH_ALL_PARAMS = "/publish?fromTime=2022-09-10T05:36:50.591&toTime=2022-09-18T05:36:50.591&stream=ProductStream"
    ACTIVITY_API_WITHOUT_FROMTIME = "/publish?toTime=2022-09-18T05:36:50.591&stream=ProductStream"
    ACTIVITY_API_WITHOUT_TOTIME = "/publish?fromTime=2022-09-10T05:36:50.591&stream=ProductStream"
    ACTIVITY_API_WITHOUT_STREAM = "/publish?fromTime=2022-09-10T05:36:50.591&toTime=2022-09-18T05:36:50.591"
    ACTIVITY_API_WITHOUT_TIME = "/publish?stream=ProductStream"
    ACTIVITY_API_FROMTIME_INVALID = "/publish?fromTime=TEST&toTime=2022-09-18T05:36:50.591&stream=ProductStream"
    ACTIVITY_API_TOTIME_INVALID = "/publish?fromTime=2022-09-10T05:36:50.591&toTime=TEST&stream=ProductStream"
    ACTIVITY_API_STREAM_INVALID = "/publish?fromTime=2022-09-10T05:36:50.591&toTime=2022-09-18T05:36:50.591&stream=TEST"
    ACTIVITY_API_WITHOUT_ALL_PARAMS = "/publish"
    files_dir = GET_publish


    def url_get_with_all_params(self):
        url = self.construct_url(self.ACTIVITY_API_WITH_ALL_PARAMS)
        return url

    def url_get_without_from_time(self):
        url = self.construct_url(self.ACTIVITY_API_WITHOUT_FROMTIME)
        return url

    def url_get_without_to_time(self):
        url = self.construct_url(self.ACTIVITY_API_WITHOUT_TOTIME)
        return url

    def url_get_without_stream(self):
        url = self.construct_url(self.ACTIVITY_API_WITHOUT_STREAM)
        return url

    def url_get_without_time(self):
        url = self.construct_url(self.ACTIVITY_API_WITHOUT_TIME)
        return url

    def url_get_with_from_time_invalid(self):
        url = self.construct_url( self.ACTIVITY_API_FROMTIME_INVALID)
        return url

    def url_get_with_to_time_invalid(self):
        url = self.construct_url( self.ACTIVITY_API_TOTIME_INVALID)
        return url

    def url_get_with_stream_invalid(self):
        url = self.construct_url( self.ACTIVITY_API_STREAM_INVALID)
        return url

    def url_get_without_all_params(self):
        url = self.construct_url( self.ACTIVITY_API_WITHOUT_ALL_PARAMS)
        return url

    def get_json_schema(self, schema):
        f = open(os.path.join(self.root_dir(self.files_dir), schema))
        json_schema = json.load(f)
        f.close()
        return json_schema
    

