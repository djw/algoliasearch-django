from django.core.management.base import BaseCommand
from django.contrib import algoliasearch


class Command(BaseCommand):
    help = 'Reindex all models to Algolia'

    def add_arguments(self, parser):
        parser.add_argument('--batchsize', nargs='?', default=1000, type=int)
        parser.add_argument('--adapter', nargs='+', type=str)

    def handle(self, *args, **options):
        '''Run the management command.'''
        self.stdout.write('The following models were reindexed:')
        print "adapters: %s" % algoliasearch.get_registered_adapters()
        for adapter in algoliasearch.get_registered_adapters():
            print "adapter: %s" % adapter
            if options.get('adapter', None) and not (
                    adapter.__name__ in options['adapter']):

                continue

            counts = adapter.reindex_all(
                batch_size=options.get('batchsize', 1000))
            self.stdout.write('\t* {} --> {}'.format(
                type(adapter).__name__, counts))
