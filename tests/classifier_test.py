"""Test the text classification classes."""
import json
from typing import List

import pytest
from twitter_ml.classify.sentiment import Sentiment


def test_basic_classification():
    """Test the classification of simple strings."""
    test_data = {"This is amazing. Wonderful. Fantastic.": 1, "This is bad.": 0}
    helper_verify_expected(test_data.keys(), test_data.values())


def test_words_with_punctuation():
    """Test that words with punctuation are taken into account during feature encoding."""
    test_data = {
        "This is amazing Wonderful Fantastic": 1,
        "This is amazing. Wonderful. Fantastic.": 1,
    }
    helper_verify_expected(test_data.keys(), test_data.values())


def test_whitespace():
    """Test that words can contain multiple spaces."""
    test_data = {"This is     amazing.      Wonderful. Fantastic.": 1}
    helper_verify_expected(test_data.keys(), test_data.values())


def test_classify_json():
    """Test the classification of JSON data to simulate tweets."""
    test_data = {
        json.loads(
            '{"created_at":"Sun Apr 07 14:01:40 +0000 2019","id":1114890989666209793,"id_str":"1114890989666209793","text":"This is amazing. Wonderful. Fantastic.","display_text_range":[46,140],"source":"\\u003ca href=\\"http:\\/\\/twitter.com\\/#!\\/download\\/ipad\\" rel=\\"nofollow\\"\\u003eTwitter for iPad\\u003c\\/a\\u003e","truncated":true,"in_reply_to_status_id":1114886297636700161,"in_reply_to_status_id_str":"1114886297636700161","in_reply_to_user_id":1016593651512770560,"in_reply_to_user_id_str":"1016593651512770560","in_reply_to_screen_name":"SmartAlecFbpe","user":{"id":868943916451721216,"id_str":"868943916451721216","name":"Alan","screen_name":"Alanling8","location":"England \\ud83c\\uddec\\ud83c\\udde7","url":null,"description":"Used to think politicians were dishonest lazy devious,have been proven right.For Brexit,anti Eu not Europe .beer and bacon but not together.English.","translator_type":"none","protected":false,"verified":false,"followers_count":2459,"friends_count":2877,"listed_count":4,"favourites_count":11198,"statuses_count":1843,"created_at":"Sun May 28 21:35:48 +0000 2017","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":"en-gb","contributors_enabled":false,"is_translator":false,"profile_background_color":"F5F8FA","profile_background_image_url":"","profile_background_image_url_https":"","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\\/\\/pbs.twimg.com\\/profile_images\\/875846141463678976\\/5Tw4kwwO_normal.jpg","profile_image_url_https":"https:\\/\\/pbs.twimg.com\\/profile_images\\/875846141463678976\\/5Tw4kwwO_normal.jpg","profile_banner_url":"https:\\/\\/pbs.twimg.com\\/profile_banners\\/868943916451721216\\/1554185469","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"quoted_status_id":1107915650104786944,"quoted_status_id_str":"1107915650104786944","quoted_status":{"created_at":"Tue Mar 19 08:04:09 +0000 2019","id":1107915650104786944,"id_str":"1107915650104786944","text":"Tony Blair admits Brexit could be a roaring success. https:\\/\\/t.co\\/vLGp7CaYIr","display_text_range":[0,52],"source":"\\u003ca href=\\"http:\\/\\/twitter.com\\/#!\\/download\\/ipad\\" rel=\\"nofollow\\"\\u003eTwitter for iPad\\u003c\\/a\\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":868943916451721216,"id_str":"868943916451721216","name":"Alan","screen_name":"Alanling8","location":"England \\ud83c\\uddec\\ud83c\\udde7","url":null,"description":"Used to think politicians were dishonest lazy devious,have been proven right.For Brexit,anti Eu not Europe .beer and bacon but not together.English.","translator_type":"none","protected":false,"verified":false,"followers_count":2459,"friends_count":2877,"listed_count":4,"favourites_count":11198,"statuses_count":1842,"created_at":"Sun May 28 21:35:48 +0000 2017","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":"en-gb","contributors_enabled":false,"is_translator":false,"profile_background_color":"F5F8FA","profile_background_image_url":"","profile_background_image_url_https":"","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\\/\\/pbs.twimg.com\\/profile_images\\/875846141463678976\\/5Tw4kwwO_normal.jpg","profile_image_url_https":"https:\\/\\/pbs.twimg.com\\/profile_images\\/875846141463678976\\/5Tw4kwwO_normal.jpg","profile_banner_url":"https:\\/\\/pbs.twimg.com\\/profile_banners\\/868943916451721216\\/1554185469","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"quote_count":0,"reply_count":0,"retweet_count":3,"favorite_count":2,"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[],"media":[{"id":1107915580588392448,"id_str":"1107915580588392448","indices":[53,76],"additional_media_info":{"monetizable":false},"media_url":"http:\\/\\/pbs.twimg.com\\/ext_tw_video_thumb\\/1107915580588392448\\/pu\\/img\\/S85795pKheXduyP_.jpg","media_url_https":"https:\\/\\/pbs.twimg.com\\/ext_tw_video_thumb\\/1107915580588392448\\/pu\\/img\\/S85795pKheXduyP_.jpg","url":"https:\\/\\/t.co\\/vLGp7CaYIr","display_url":"pic.twitter.com\\/vLGp7CaYIr","expanded_url":"https:\\/\\/twitter.com\\/Alanling8\\/status\\/1107915650104786944\\/video\\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"small":{"w":383,"h":680,"resize":"fit"},"large":{"w":720,"h":1280,"resize":"fit"},"medium":{"w":675,"h":1200,"resize":"fit"}}}]},"extended_entities":{"media":[{"id":1107915580588392448,"id_str":"1107915580588392448","indices":[53,76],"additional_media_info":{"monetizable":false},"media_url":"http:\\/\\/pbs.twimg.com\\/ext_tw_video_thumb\\/1107915580588392448\\/pu\\/img\\/S85795pKheXduyP_.jpg","media_url_https":"https:\\/\\/pbs.twimg.com\\/ext_tw_video_thumb\\/1107915580588392448\\/pu\\/img\\/S85795pKheXduyP_.jpg","url":"https:\\/\\/t.co\\/vLGp7CaYIr","display_url":"pic.twitter.com\\/vLGp7CaYIr","expanded_url":"https:\\/\\/twitter.com\\/Alanling8\\/status\\/1107915650104786944\\/video\\/1","type":"video","video_info":{"aspect_ratio":[9,16],"duration_millis":10075,"variants":[{"bitrate":632000,"content_type":"video\\/mp4","url":"https:\\/\\/video.twimg.com\\/ext_tw_video\\/1107915580588392448\\/pu\\/vid\\/320x568\\/MFDFiangPwAO8HSG.mp4?tag=8"},{"bitrate":2176000,"content_type":"video\\/mp4","url":"https:\\/\\/video.twimg.com\\/ext_tw_video\\/1107915580588392448\\/pu\\/vid\\/720x1280\\/L2IGqOVlYEjQUFSn.mp4?tag=8"},{"bitrate":832000,"content_type":"video\\/mp4","url":"https:\\/\\/video.twimg.com\\/ext_tw_video\\/1107915580588392448\\/pu\\/vid\\/360x640\\/rPtwQp53Xt1VTv7Z.mp4?tag=8"},{"content_type":"application\\/x-mpegURL","url":"https:\\/\\/video.twimg.com\\/ext_tw_video\\/1107915580588392448\\/pu\\/pl\\/_mVhLHeacFpAaEcp.m3u8?tag=8"}]},"sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"small":{"w":383,"h":680,"resize":"fit"},"large":{"w":720,"h":1280,"resize":"fit"},"medium":{"w":675,"h":1200,"resize":"fit"}}}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"en"},"quoted_status_permalink":{"url":"https:\\/\\/t.co\\/wxWo9i52KY","expanded":"https:\\/\\/twitter.com\\/alanling8\\/status\\/1107915650104786944?s=21","display":"twitter.com\\/alanling8\\/stat\\u2026"},"is_quote_status":true,"extended_tweet":{"full_text":"@SmartAlecFbpe @LeaveEUOfficial @Nigel_Farage https:\\/\\/t.co\\/wxWo9i52KY.   Here\\u2019s Tony Blair the biggest remainer admitting Brexit could be a huge success.","display_text_range":[46,153],"entities":{"hashtags":[],"urls":[{"url":"https:\\/\\/t.co\\/wxWo9i52KY","expanded_url":"https:\\/\\/twitter.com\\/alanling8\\/status\\/1107915650104786944?s=21","display_url":"twitter.com\\/alanling8\\/stat\\u2026","indices":[46,69]}],"user_mentions":[{"screen_name":"SmartAlecFbpe","name":"Alec Hunter \\ud83c\\uddea\\ud83c\\uddfa","id":1016593651512770560,"id_str":"1016593651512770560","indices":[0,14]},{"screen_name":"LeaveEUOfficial","name":"Leave.EU","id":3362016513,"id_str":"3362016513","indices":[15,31]},{"screen_name":"Nigel_Farage","name":"Nigel Farage","id":19017675,"id_str":"19017675","indices":[32,45]}],"symbols":[]}},"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[{"url":"https:\\/\\/t.co\\/wxWo9i52KY","expanded_url":"https:\\/\\/twitter.com\\/alanling8\\/status\\/1107915650104786944?s=21","display_url":"twitter.com\\/alanling8\\/stat\\u2026","indices":[46,69]},{"url":"https:\\/\\/t.co\\/Tzc5OK1UPE","expanded_url":"https:\\/\\/twitter.com\\/i\\/web\\/status\\/1114890989666209793","display_url":"twitter.com\\/i\\/web\\/status\\/1\\u2026","indices":[117,140]}],"user_mentions":[{"screen_name":"SmartAlecFbpe","name":"Alec Hunter \\ud83c\\uddea\\ud83c\\uddfa","id":1016593651512770560,"id_str":"1016593651512770560","indices":[0,14]},{"screen_name":"LeaveEUOfficial","name":"Leave.EU","id":3362016513,"id_str":"3362016513","indices":[15,31]},{"screen_name":"Nigel_Farage","name":"Nigel Farage","id":19017675,"id_str":"19017675","indices":[32,45]}],"symbols":[]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"en","timestamp_ms":"1554645700266"}\r\n'
        )["text"]: 1
    }
    helper_verify_expected(test_data.keys(), test_data.values())


def test_missing_config():
    """Test that a Sentiment class can only be instantiated with a valid configuration file."""
    with pytest.raises(FileNotFoundError):
        Sentiment("missing.yaml")


def test_no_sub_classifiers():
    """Test that a voting classifier cannot have 0 sub-classifiers."""
    with pytest.raises(KeyError):
        Sentiment("tests/test_0_classifiers.yaml")


def helper_verify_expected(samples: List[str], expected: List[int]):
    """Classify each item of a list and assert this equals the expected results.

    :param samples: list of text samples to classify
    :param expected: list of expected classifications
    """
    classifier = Sentiment("tests/test_voting.yaml")
    for text, expected_classification in zip(samples, expected):
        _, _, sentiment = classifier.classify_sentiment(text)
        print("%s\nClassification: %s" % (text, sentiment))
        assert sentiment == expected_classification
