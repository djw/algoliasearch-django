'''
AlgoliaSearch integration for Django.
http://www.algolia.com
'''

from __future__ import unicode_literals

from django.contrib.algoliasearch.models import AlgoliaIndex, model_name
from django.contrib.algoliasearch.registration import AlgoliaEngine
from django.contrib.algoliasearch.registration import algolia_engine

algolia_engine = algolia_engine
register = algolia_engine.register
unregister = algolia_engine.unregister
get_registered_model = algolia_engine.get_registered_models
get_registered_adapters = algolia_engine.get_registered_adapters
get_adapter = algolia_engine.get_adapter
raw_search = algolia_engine.raw_search
