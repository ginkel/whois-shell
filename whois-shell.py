#!/usr/bin/python

from cmd import Cmd
import pywhois

class WhoisShellCmd(Cmd):
	TLDs = ['.com', '.de', '.io', '.net', '.org', '.se']

	def __init__(self):
		Cmd.__init__(self)
		self.prompt = "$ "
	def do_quit(self, message):
		print "Bye, bye..."
		return 1
	def do_EOF(self, message):
		print "\nBye, bye..."
		return 1
	def default(self, domain):
		if domain.find('.') > -1:
			print pywhois.whois(domain).text
		else:
			for tld in self.TLDs:
				self.whois("%s%s" % (domain, tld))
	def completedefault(self, text, line, begidx, endidx):
		if not '.' in text:
			return TLDs
		else:
			return []
	def whois(self, domain):
                try:
                        w = pywhois.whois(domain)
                        print "%s: registered" % domain
                except pywhois.parser.PywhoisError:
                        print "%s: FREE" % domain

if __name__ == "__main__":
	shell = WhoisShellCmd()
	shell.cmdloop('Whois Shell v0.1\n- Enter any domain name to check its availability.\n- Enter a domain name without a TLD to query multiple registries.\n')
