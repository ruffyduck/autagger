"""Entry point for AuTag"""

import sys, getopt, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from autag.controller.auclean import AutoCleanup
from autag.controller.aucrawl import AutoCrawler
from autag.controller.audefault import AutoDefault
from autag.controller.auimage import AutoImage
from autag.controller.aumove import AutoMove
from autag.controller.aunumber import AutoNumbers
from autag.controller.auremove import AutoRemoval
from autag.controller.aurename import AutoRename
from autag.controller.autagger import AutoTagger
from autag.controller.repltag import ReplaceTag
from autag.model.audict import build_auto_dicts
from autag.model.basetag import get_tag
from autagger.view.augui import AuGUI


def main(argv):
	try:
		opts, _ = getopt.getopt(argv, "hd:", ["-help","directory="])
	except getopt.GetoptError as e:
		print(e)
		sys.exit(2)

	dir = None
	for opt, arg in opts:
		if opt == '-h':
			print("Pass '-d' or 'directory=' to tag files in given directory")
			sys.exit()
		elif opt in ('-d', '-directory'):
			dir = arg

	audicts = build_auto_dicts("resources/autodicts.json")
	auto_tag = AutoTagger()
	auto_tag.add_auto_tags([AutoImage(), AutoCleanup(), AutoNumbers(),
	                        AutoCrawler("UVtLSggkngYRiFHyFSdnjrgaFufcXmWIjrhiPkiN",
	                                    [get_tag("GENRE"),
	                                     get_tag("ORGANIZATION")],
	                                    audicts),
	                        ReplaceTag(audicts["GENRE"], get_tag("GENRE")),
	                        ReplaceTag(audicts["TITLE"], get_tag("TITLE")),
	                        AutoRemoval("resources/autoremove.json"),
	                        AutoDefault("resources/defaultvalues.json")])

	auto_file = AutoTagger()
	auto_file.add_auto_tags([AutoRename()])  #, AutoMove("D:/Musik/")])

	gui = AuGUI(auto_tag, auto_file, dir)
	gui.draw()


if __name__== "__main__":
	main(sys.argv[1:])
