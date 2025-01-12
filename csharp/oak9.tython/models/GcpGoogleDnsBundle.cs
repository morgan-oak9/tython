// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: gcp/gcp_google_dns_bundle.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Gcp.GoogleDnsBundle {

  /// <summary>Holder for reflection information generated from gcp/gcp_google_dns_bundle.proto</summary>
  public static partial class GcpGoogleDnsBundleReflection {

    #region Descriptor
    /// <summary>File descriptor for gcp/gcp_google_dns_bundle.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GcpGoogleDnsBundleReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Ch9nY3AvZ2NwX2dvb2dsZV9kbnNfYnVuZGxlLnByb3RvEiFvYWs5LnR5dGhv",
            "bi5nY3AuZ29vZ2xlX2Ruc19idW5kbGUaE3NoYXJlZC9zaGFyZWQucHJvdG8a",
            "EWdjcC9nY3BfZG5zLnByb3RvIrkBCglHb29nbGVEbnMSPQoQZG5zX21hbmFn",
            "ZWRfem9uZRgBIAEoCzIjLm9hazkudHl0aG9uLmdjcC5kbnMuRG5zTWFuYWdl",
            "ZFpvbmUSMgoKZG5zX3BvbGljeRgCIAEoCzIeLm9hazkudHl0aG9uLmdjcC5k",
            "bnMuRG5zUG9saWN5EjkKDmRuc19yZWNvcmRfc2V0GAMgASgLMiEub2FrOS50",
            "eXRob24uZ2NwLmRucy5EbnNSZWNvcmRTZXRiBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, global::Oak9.Tython.Gcp.Dns.GcpDnsReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.GoogleDnsBundle.GoogleDns), global::Oak9.Tython.Gcp.GoogleDnsBundle.GoogleDns.Parser, new[]{ "DnsManagedZone", "DnsPolicy", "DnsRecordSet" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class GoogleDns : pb::IMessage<GoogleDns>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<GoogleDns> _parser = new pb::MessageParser<GoogleDns>(() => new GoogleDns());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<GoogleDns> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.GoogleDnsBundle.GcpGoogleDnsBundleReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleDns() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleDns(GoogleDns other) : this() {
      dnsManagedZone_ = other.dnsManagedZone_ != null ? other.dnsManagedZone_.Clone() : null;
      dnsPolicy_ = other.dnsPolicy_ != null ? other.dnsPolicy_.Clone() : null;
      dnsRecordSet_ = other.dnsRecordSet_ != null ? other.dnsRecordSet_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleDns Clone() {
      return new GoogleDns(this);
    }

    /// <summary>Field number for the "dns_managed_zone" field.</summary>
    public const int DnsManagedZoneFieldNumber = 1;
    private global::Oak9.Tython.Gcp.Dns.DnsManagedZone dnsManagedZone_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.Dns.DnsManagedZone DnsManagedZone {
      get { return dnsManagedZone_; }
      set {
        dnsManagedZone_ = value;
      }
    }

    /// <summary>Field number for the "dns_policy" field.</summary>
    public const int DnsPolicyFieldNumber = 2;
    private global::Oak9.Tython.Gcp.Dns.DnsPolicy dnsPolicy_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.Dns.DnsPolicy DnsPolicy {
      get { return dnsPolicy_; }
      set {
        dnsPolicy_ = value;
      }
    }

    /// <summary>Field number for the "dns_record_set" field.</summary>
    public const int DnsRecordSetFieldNumber = 3;
    private global::Oak9.Tython.Gcp.Dns.DnsRecordSet dnsRecordSet_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.Dns.DnsRecordSet DnsRecordSet {
      get { return dnsRecordSet_; }
      set {
        dnsRecordSet_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as GoogleDns);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(GoogleDns other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(DnsManagedZone, other.DnsManagedZone)) return false;
      if (!object.Equals(DnsPolicy, other.DnsPolicy)) return false;
      if (!object.Equals(DnsRecordSet, other.DnsRecordSet)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (dnsManagedZone_ != null) hash ^= DnsManagedZone.GetHashCode();
      if (dnsPolicy_ != null) hash ^= DnsPolicy.GetHashCode();
      if (dnsRecordSet_ != null) hash ^= DnsRecordSet.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (dnsManagedZone_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(DnsManagedZone);
      }
      if (dnsPolicy_ != null) {
        output.WriteRawTag(18);
        output.WriteMessage(DnsPolicy);
      }
      if (dnsRecordSet_ != null) {
        output.WriteRawTag(26);
        output.WriteMessage(DnsRecordSet);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (dnsManagedZone_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(DnsManagedZone);
      }
      if (dnsPolicy_ != null) {
        output.WriteRawTag(18);
        output.WriteMessage(DnsPolicy);
      }
      if (dnsRecordSet_ != null) {
        output.WriteRawTag(26);
        output.WriteMessage(DnsRecordSet);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (dnsManagedZone_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(DnsManagedZone);
      }
      if (dnsPolicy_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(DnsPolicy);
      }
      if (dnsRecordSet_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(DnsRecordSet);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(GoogleDns other) {
      if (other == null) {
        return;
      }
      if (other.dnsManagedZone_ != null) {
        if (dnsManagedZone_ == null) {
          DnsManagedZone = new global::Oak9.Tython.Gcp.Dns.DnsManagedZone();
        }
        DnsManagedZone.MergeFrom(other.DnsManagedZone);
      }
      if (other.dnsPolicy_ != null) {
        if (dnsPolicy_ == null) {
          DnsPolicy = new global::Oak9.Tython.Gcp.Dns.DnsPolicy();
        }
        DnsPolicy.MergeFrom(other.DnsPolicy);
      }
      if (other.dnsRecordSet_ != null) {
        if (dnsRecordSet_ == null) {
          DnsRecordSet = new global::Oak9.Tython.Gcp.Dns.DnsRecordSet();
        }
        DnsRecordSet.MergeFrom(other.DnsRecordSet);
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            if (dnsManagedZone_ == null) {
              DnsManagedZone = new global::Oak9.Tython.Gcp.Dns.DnsManagedZone();
            }
            input.ReadMessage(DnsManagedZone);
            break;
          }
          case 18: {
            if (dnsPolicy_ == null) {
              DnsPolicy = new global::Oak9.Tython.Gcp.Dns.DnsPolicy();
            }
            input.ReadMessage(DnsPolicy);
            break;
          }
          case 26: {
            if (dnsRecordSet_ == null) {
              DnsRecordSet = new global::Oak9.Tython.Gcp.Dns.DnsRecordSet();
            }
            input.ReadMessage(DnsRecordSet);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            if (dnsManagedZone_ == null) {
              DnsManagedZone = new global::Oak9.Tython.Gcp.Dns.DnsManagedZone();
            }
            input.ReadMessage(DnsManagedZone);
            break;
          }
          case 18: {
            if (dnsPolicy_ == null) {
              DnsPolicy = new global::Oak9.Tython.Gcp.Dns.DnsPolicy();
            }
            input.ReadMessage(DnsPolicy);
            break;
          }
          case 26: {
            if (dnsRecordSet_ == null) {
              DnsRecordSet = new global::Oak9.Tython.Gcp.Dns.DnsRecordSet();
            }
            input.ReadMessage(DnsRecordSet);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code
